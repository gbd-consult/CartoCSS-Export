from qgis.core import *
import layer
import debug
import error
import os


def layers(prj):
    for la in groups(prj.layerTreeRoot()):
        yield la


def groups(group):
    for tl in group.children():
        if not tl.isVisible():
            continue
        if isinstance(tl, QgsLayerTreeGroup):
            for la in groups(tl):
                yield la
        else:
            yield tl.layer()


def file_name(prj):
    fn = prj.fileName()
    if not fn:
        return 'Untitled'
    _, fn = os.path.split(fn)
    fn, _ = os.path.splitext(fn)
    return fn


def global_metadata(cc, prj):
    return {
        "format": "png24",
        "interactivity": False,
        "minzoom": 0,
        "maxzoom": 22,
        "scale": 1,
        "metatile": 2,
        "name": file_name(prj),
        "description": ""
    }


def compute_bounds(cc, prj):
    bounds = None

    for la in layers(prj):
        ex = la.extent()
        if ex:
            r = [ex.xMinimum(), ex.yMinimum(), ex.xMaximum(), ex.yMaximum()]
            if not bounds:
                bounds = r
            else:
                bounds = [
                    min(bounds[0], r[0]),
                    min(bounds[1], r[1]),
                    max(bounds[2], r[2]),
                    max(bounds[3], r[3]),
                ]

    return bounds


CartoSrid = 4326  # WGS 84


def metadata(cc, prj):
    layer_meta = []
    crs = None

    for la in layers(prj):
        lm = layer.metadata(cc, la)
        if lm:
            layer_meta.append(lm)
            if '_crs_object' in lm:
                crs = lm['_crs_object']

    if not layer_meta:
        cc.error(error.EMPTY_PROJECT)

    d = global_metadata(cc, prj)

    d['Stylesheet'] = ['style.mss']

    # NB: carto renders top down
    d['Layer'] = layer_meta[::-1]

    if crs:
        bounds = compute_bounds(cc, prj)
        if bounds:
            tr = QgsCoordinateTransform(crs, QgsCoordinateReferenceSystem(CartoSrid))
            p1 = tr.transform(bounds[0], bounds[1])
            p2 = tr.transform(bounds[2], bounds[3])

            d['bounds'] = [
                p1.x(), p1.y(),
                p2.x(), p2.y(),
            ]

            d['center'] = [
                p1.x() + (p2.x() - p1.x()) * 0.5,
                p1.y() + (p2.y() - p1.y()) * 0.5,
                11
            ]

    return d


def exportQgsProject(cc, prj):
    rules = []
    for la in layers(prj):
        cc.enter_layer(la)
        rules.append(cc.export(la))
        cc.leave_layer()
    return rules
