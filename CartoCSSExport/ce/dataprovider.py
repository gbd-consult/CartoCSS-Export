"""Handle QGIS data providers."""

from qgis.core import *

import defs, error, debug


def _srs(dp, meta):
    meta['_crs_object'] = dp.crs()
    meta['srs'] = dp.crs().toProj4()
    meta['srs-name'] = dp.crs().authid()


def meta_gdal(cc, dp, meta):
    _srs(dp, meta)
    meta['geometry'] = 'raster'
    meta['Datasource'] = {
        'file': dp.dataSourceUri()
    }


def meta_ogr(cc, dp, meta):
    _srs(dp, meta)
    meta['geometry'] = defs.WkbType[dp.geometryType()]
    # uri is like path|layerid=0
    uri = dp.dataSourceUri()
    meta['Datasource'] = {
        'file': uri.split('|')[0]
    }


def meta_postgres(cc, dp, meta):
    _srs(dp, meta)
    meta['geometry'] = defs.WkbType[dp.geometryType()]
    ds = QgsDataSourceURI(dp.dataSourceUri())
    key = ds.keyColumn()
    if key == 'tid':
        key = ''
    meta['Datasource'] = {
        'type': 'postgis',
        '_orig_table': ds.quotedTablename(),
        'table': '(SELECT * FROM %s) AS t' % ds.quotedTablename(),
        'key_field': key,
        'geometry_field': ds.geometryColumn(),
        'dbname': ds.database(),
        'host': ds.host(),
        'port': ds.port(),
        'user': ds.username(),
        'password': ds.password(),
        'extent_cache': 'dynamic',
        'extent': ''
    }


def metadata(cc, dp, meta):
    if dp is None:
        raise ValueError

    name = dp.name()
    fn = globals().get('meta_' + name)
    if fn:
        fn(cc, dp, meta)
        return True
    cc.error(error.DATA_PROVIDER_NOT_IMPLEMENTED, name)
