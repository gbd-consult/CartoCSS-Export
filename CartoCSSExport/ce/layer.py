# coding=utf8

"""Layer converter."""

import re

import qgis.PyQt.QtXml as Qx
from qgis.core import *

import dataprovider
import labeling


def xml2dict(node):
    """Convert an XML node to a dict(name, attributes, value, children)."""

    def attrs(node):
        d = {}
        na = node.attributes()
        for n in range(na.length()):
            a = na.item(n)
            d[a.nodeName()] = a.nodeValue()
        return d

    d = {
        'name': node.nodeName(),
        'attributes': attrs(node),
        'value': node.nodeValue(),
        'children': []
    }

    cn = node.childNodes()
    for n in range(cn.length()):
        d['children'].append(xml2dict(cn.item(n)))

    return d


def to_dict(la):
    """Create an xml-based dict from the layer object.
    
    :param la: QgsVectorLayer 
    :rtype: dict 
    """

    doc = Qx.QDomDocument()
    layer_node = doc.createElement('maplayer')

    doc.appendChild(layer_node)
    ok = la.writeXml(layer_node, doc)

    return xml2dict(layer_node)


_umlauts = {
    u'ä': 'ae',
    u'ö': 'oe',
    u'ü': 'ue',
    u'Ä': 'AE',
    u'Ö': 'OE',
    u'Ü': 'UE',
    u'ß': 'ss',
}


def id_of(la):
    s = la.id()
    for k, v in _umlauts.items():
        s = s.replace(k, v)
    return re.sub(r'[^A-Za-z0-9]+', '_', s)


def metadata(cc, la):
    meta = {
        'srs-name': 'custom',
        'id': id_of(la),
        'name': id_of(la),
        '_id': la.id(),

    }

    if dataprovider.metadata(cc, la.dataProvider(), meta):
        return meta


def exportQgsVectorLayer(cc, la):
    sub = [cc.export(la.rendererV2())]

    # Since there's no python API for labeling V2, read props from the layer XML.
    lab = labeling.from_layer_dict(to_dict(la))
    if lab:
        sub.append(cc.export(lab))

    r = cc.rule('VectorLayer', id=id_of(la), layer=la, sub=sub)

    if la.hasScaleBasedVisibility():
        r.zoom = [la.minimumScale(), la.maximumScale()]

    return r


def exportQgsRasterLayer(cc, la):
    return cc.rule('RasterLayer', id=id_of(la), layer=la, props={
        'raster-opacity': ('float', 1)
    })
