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


def extract(prj, x, y, bounds, srid):
    with open(prj) as fp:
        text = fp.read()

    xy = '%04d_%04d' % (x, y)
    log('extracting', xy)
    counts = {}

    for tab in tables:
        new_tab = tab + '_' + xy

        text = re.sub(r'(table=.+?)"%s"' % tab, r'\1"' + new_tab + '"', text)
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
            db_exec('''
                UPDATE %s 
                    SET wkb_geometry = ST_Multi(ST_CollectionExtract(
                        ST_Intersection(wkb_geometry, %s),
                        3)) 
            ''' % (new_tab, mkenv))

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


def do_split(prj, xsteps, ysteps, envelope):
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

    try:
        prj = argv[1]
        drop = argv[2] == 'drop'
        if not drop:
            xsteps = int(argv[2])
            ysteps = int(argv[3])
            if len(argv) > 4:
                envelope = map(float, argv[4].split())

    except:
        print 'usage: split_project.py project-path xsteps ysteps <envelope>'
        print 'usage: split_project.py project-path drop'
        sys.exit(1)

    if drop:
        do_drop(prj)
    else:
        do_split(prj, xsteps, ysteps, envelope)


if __name__ == '__main__':
    main(sys.argv)
