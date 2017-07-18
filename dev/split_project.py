"""Split a qgis project with large postgis tables into smaller rectangular chunks."""

import re
import sys
import os
import glob

import psycopg2

tables = [
    'flaechen',
    'gewaesser',
    'gewaesserflaechen',
    'grenzen',
    'punkte',
    'strassen',
]

_db_connection = None


def log(*args):
    for a in args:
        sys.stdout.write(' %s' % a)
        sys.stdout.flush()


def db_connect(params):
    global _db_connection

    _db_connection = psycopg2.connect(
        database=params['dbname'],
        user=params['user'],
        password=params['password'],
        host=params['host'],
        port=params['port']
    )
    _db_connection.autocommit = True


def db_exec(sql, params=None):
    cur = _db_connection.cursor()

    try:
        cur.execute(sql, params)

        if sql.strip().upper().startswith('SELECT'):
            cnames = [c.name for c in cur.description]
            return [dict(zip(cnames, rec)) for rec in cur]

    except:
        log('FAULTY sql:', sql, '\n')
        raise

    finally:
        cur.close()


def read_db_params(prj):
    with open(prj) as fp:
        text = fp.read()
        for p in re.findall(r'<datasource>(.+?)</datasource>', text):
            if 'dbname' in p:
                d = {}
                for k, v in re.findall(r'(\w+)=(\S+)', p):
                    if v.startswith("'"):
                        v = v[1:-1]
                    d[k] = v
                return d


def compute_envelope():
    coords = []

    for tab in tables:
        log(tab)
        rs = db_exec('SELECT ST_Extent(wkb_geometry) AS e FROM %s' % tab)
        coords.append(map(float, re.findall(r'\d+(?:\.\d+)?', rs[0]['e'])))
    coords = zip(*coords)

    log('\n')

    return (
        min(coords[0]),
        min(coords[1]),
        max(coords[2]),
        max(coords[3])
    )


def area_intersections(new_tab, mkenv, srid):
    db_exec('''
        ALTER TABLE %s 
            ADD COLUMN inter_wkt TEXT, 
            ADD COLUMN inter_geom GEOMETRY(MultiPolygon,%s)
    ''' % (new_tab, srid))

    db_exec('''
        UPDATE %s 
            SET inter_wkt = ST_AsText(ST_Intersection(wkb_geometry, %s))
    ''' % (new_tab, mkenv))

    db_exec('''
        UPDATE %s 
            SET inter_geom = ST_GeomFromText(inter_wkt,%s)
            WHERE inter_wkt LIKE 'MULTIPOLYGON%%'
    ''' % (new_tab, srid))

    db_exec('''
        UPDATE %s 
            SET inter_geom = ST_Multi(ST_GeomFromText(inter_wkt,%s))
            WHERE inter_wkt LIKE 'POLYGON%%'
    ''' % (new_tab, srid))

    c1 = db_exec('SELECT COUNT(*) AS c FROM %s' % new_tab)[0]['c']

    db_exec('''
        DELETE FROM %s 
            WHERE inter_geom IS NULL
    ''' % (new_tab,))

    c2 = db_exec('SELECT COUNT(*) AS c FROM %s' % new_tab)[0]['c']

    if c1 - c2:
        log('[bad_geom=%d]' % (c1 - c2))

    db_exec('''
        UPDATE %s 
            SET wkb_geometry = inter_geom
    ''' % (new_tab,))

    db_exec('''
        ALTER TABLE %s 
            DROP COLUMN inter_wkt
    ''' % (new_tab,))

    db_exec('''
        ALTER TABLE %s 
            DROP COLUMN inter_geom
    ''' % (new_tab,))


def extract(prj, x, y, bounds, srid):
    with open(prj) as fp:
        text = fp.read()

    xy = '%04d_%04d' % (x, y)
    log('extracting', xy)
    counts = {}

    for tab in tables:
        new_tab = tab + '_' + xy

        text = re.sub(r'(table=.+?)"%s"' % tab, r'\1"%s"' % new_tab, text)
        mkenv = 'ST_MakeEnvelope(%f, %f, %f, %f, %s)' % (
            bounds[0],
            bounds[1],
            bounds[2],
            bounds[3],
            srid)

        db_exec('DROP TABLE IF EXISTS %s' % new_tab)
        db_exec('''
            CREATE TABLE %s AS 
                SELECT * FROM %s 
                    WHERE ST_Intersects(wkb_geometry, %s) 
        ''' % (new_tab, tab, mkenv))

        if tab in ('grenzen', 'flaechen'):
            area_intersections(new_tab, mkenv, srid)

        r = db_exec('SELECT COUNT(*) AS c FROM %s' % new_tab)
        counts[tab] = int(r[0]['c'])
        # log(tab, '(%s)' % c)

    if sum(counts.values()) == 0:
        log('EMPTY\n')
        for tab in tables:
            new_tab = tab + '_' + xy
            db_exec('DROP TABLE IF EXISTS %s' % new_tab)
        return

    new_prj = prj.replace('.qgs', '_' + xy + '.qgs')
    with open(new_prj, 'w') as fp:
        fp.write(text)

    log('ok', repr(counts), '\n')


def do_split(prj, xsteps, ysteps, envelope, onlyx, onlyy):
    params = read_db_params(prj)
    srid = params['srid']

    db_connect(params)

    if not envelope:
        log('computing envelope \n')
        envelope = compute_envelope()

    xmin, ymin, xmax, ymax = envelope
    xsize = (xmax - xmin) / float(xsteps)
    ysize = (ymax - ymin) / float(ysteps)

    log('envelope is', xmin, ymin, xmax, ymax, '\n')

    for y in range(ysteps):
        for x in range(xsteps):
            if onlyx is not None and x != onlyx:
                continue
            if onlyy is not None and y != onlyy:
                continue
            bounds = xmin + xsize * x, ymin + ysize * y, xmin + xsize * (x + 1), ymin + ysize * (y + 1)
            extract(prj, x, y, bounds, srid)


def do_drop(prj):
    params = read_db_params(prj)
    db_connect(params)

    tab_pattern = r'^(%s)_(\d{4})_(\d{4})$' % '|'.join(tables)
    cnt = 0

    for r in db_exec('select * from information_schema.tables'):
        if re.match(tab_pattern, r['table_name']):
            db_exec('DROP TABLE %s' % r['table_name'])
            cnt += 1

    log(cnt, 'tables removed\n')

    base, fn = os.path.split(prj)
    file_pattern = r'/%s_(\d{4})_(\d{4})\.qgs$' % os.path.splitext(fn)[0]
    cnt = 0

    for path in glob.glob(base + '/*.qgs'):
        if re.search(file_pattern, path):
            os.unlink(path)
            cnt += 1

    log(cnt, 'files removed\n')


def main(argv):
    xsteps = ysteps = envelope = None
    onlyx = onlyy = None

    try:
        prj = argv[1]
        drop = argv[2] == 'drop'
        if not drop:
            xsteps = int(argv[2])
            ysteps = int(argv[3])
            if len(argv) > 4:
                envelope = map(float, argv[4].split())
            if len(argv) > 5:
                onlyx = int(argv[5])
                onlyy = int(argv[6])

    except:
        print 'usage: split_project.py project-path xsteps ysteps <envelope> <onlyX> <onlyY>'
        print 'usage: split_project.py project-path drop'
        sys.exit(1)

    if drop:
        do_drop(prj)
    else:
        do_split(prj, xsteps, ysteps, envelope, onlyx, onlyy)


if __name__ == '__main__':
    main(sys.argv)
