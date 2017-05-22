"""Converters for Qgs Symbols."""

import defs, style


def exportQgsSymbolV2(cc, sym):
    sub = [cc.export(sla) for sla in sym.symbolLayers()]
    return cc.rule(defs.SymbolType[int(sym.type())] + 'Symbol', sub=sub)


def exportQgsFillSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsMarkerSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsLineSymbolV2(cc, sym):
    return exportQgsSymbolV2(cc, sym)


def exportQgsSimpleFillSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'outline, fill')
    return cc.rule(sla.layerType(), props=props)


def exportQgsSimpleLineSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'line')
    return cc.rule(sla.layerType(), props=props)


def exportQgsSimpleMarkerSymbolLayerV2(cc, sla):
    props = style.convert(cc, sla, 'marker')
    return cc.rule(sla.layerType(), props=props)


def exportQgsCentroidFillSymbolLayerV2(cc, sla):
    return cc.export(sla.subSymbol())
