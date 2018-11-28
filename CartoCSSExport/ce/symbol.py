"""Converters for Qgs Symbols."""

import defs, style, debug


def exportQgsSymbolV2(cc, sym):
    props = {}

    alpha = sym.alpha()
    if alpha < 1:
        props['opacity'] = 'float', alpha

    sub = [cc.export(sla) for sla in sym.symbolLayers()]
    return cc.clause(sym, defs.SymbolType[int(sym.type())] + 'Symbol', props=props, sub=sub)


def exportQgsFillSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsMarkerSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsLineSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsSimpleFillSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'outline, fill')
    return cc.clause(sla, sla.layerType(), props=props)


def exportQgsSimpleLineSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'line')
    return cc.clause(sla, sla.layerType(), props=props)


def exportQgsSimpleMarkerSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'marker')
    return cc.clause(sla, sla.layerType(), props=props)


def exportQgsCentroidFillSymbolLayerV2(cc, sla):
    return cc.export(sla.subSymbol())
