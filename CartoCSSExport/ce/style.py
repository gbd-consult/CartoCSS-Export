"""Map Qgis style props to Carto."""

import debug
import error
import defs

Unit = ['', 'Pixel', 'MM', 'MapUnit']
LineStyle = ['solid', 'no', 'dash', 'dot', 'dash dot', 'dash dot dot']


class SymbolLayerProps:
    bufferDraw = 0
    bufferColor = 0
    bufferSize = 0
    capstyle = ['square', 'flat', 'round']
    color = 0
    customdash_unit = Unit
    fieldName = ''
    fontFamily = ''
    fontSize = 0
    fontSizeInMapUnits = 0
    isExpression = 0
    joinstyle = ['miter', 'bevel', 'round']
    line_color = 0
    line_style = LineStyle
    line_width = 0
    line_width_unit = Unit
    name = ['arrow', 'circle']
    namedStyle = ''
    offset = 0
    offset_unit = Unit
    outline_color = 0
    outline_style = LineStyle
    outline_width = 0
    outline_width_unit = Unit
    placement = ['AroundPoint', 'Line', 'Curved', 'Horizontal', 'Free']
    size = 0
    size_unit = Unit
    # @todo: implement with polygon-pattern-file
    # "horizontal","vertical","cross","b_diagonal","f_diagonal","diagonal_x","dense1..7 #
    style = ['solid', 'no']
    textColor = 0
    use_custom_dash = 0


ResolveDefs = {
    'placement': 'Placement'

}


def symbol_props(cc, sla):
    p = SymbolLayerProps()
    typ = sla.layerType()
    defaults = defs.Defaults.get(typ, {})

    for name, val in sla.properties().items():
        if val == defaults.get(name):
            # debug.pp(['default', name, val])
            continue

        prop = '%s.%s' % (typ, name)
        info = '%s.%s=%s' % (typ, name, val)

        if not hasattr(p, name):
            # debug.pp([prop, val])
            cc.error(error.PROP_NOT_IMPLEMENTED, prop)
            continue

        if name in ResolveDefs:
            val = getattr(defs, ResolveDefs[name]).get(int(val))
            if not val:
                cc.error(error.VALUE_NOT_IMPLEMENTED, info)
                continue

        known_values = getattr(p, name)
        if isinstance(known_values, list) and val not in known_values:
            cc.error(error.VALUE_NOT_IMPLEMENTED, info)
            setattr(p, name, '')
            continue

        setattr(p, name, val)

    for name in dir(p):
        val = getattr(p, name)
        if isinstance(val, list):
            setattr(p, name, val[0])

    return p


def do_line_style(cc, style, d):
    if style == 'dash':
        d['line-dasharray'] = 'list', [10, 4]
    if style == 'dot':
        d['line-dasharray'] = 'list', [4, 4]
    if style == 'dash dot':
        d['line-dasharray'] = 'list', [10, 4, 4, 4]
    if style == 'dash dot dot':
        d['line-dasharray'] = 'list', [10, 4, 4, 4, 4, 4]


def do_outline(cc, p, d):
    if p.outline_style == 'no':
        return

    do_line_style(cc, p.outline_style, d)

    d['line-width'] = 'size', [p.outline_width, p.outline_width_unit]
    d['line-color'] = 'color', p.outline_color

    if p.joinstyle:
        d['line-join'] = 'string', p.joinstyle


def do_fill(cc, p, d):
    if p.style == 'no':
        return
    d['polygon-fill'] = 'color', p.color


def do_line(cc, p, d):
    if p.line_style == 'no':
        return

    do_line_style(cc, p.line_style, d)

    d['line-width'] = 'size', [p.line_width, p.line_width_unit]
    if p.offset:
        d['line-offset'] = 'size', [p.offset, p.offset_unit]

    d['line-color'] = 'color', p.line_color

    if p.joinstyle:
        d['line-join'] = 'string', p.joinstyle

    if p.capstyle == 'flat':
        d['line-cap'] = 'string', 'butt'
    if p.capstyle in ('round', 'square'):
        d['line-cap'] = 'string', p.capstyle


def do_marker(cc, p, d):
    d['marker-fill'] = 'color', p.color
    d['marker-width'] = 'size', [p.size, p.size_unit]
    d['marker-height'] = 'size', [p.size, p.size_unit]

    if p.name == 'circle':
        d['marker-type'] = 'string', 'ellipse'
    if p.name == 'arrow':
        d['marker-type'] = 'string', 'arrow'


def do_label(cc, p, d):
    if p.placement == 'AroundPoint':
        d['text-placement'] = 'point'
    if p.placement == 'Line':
        d['text-placement'] = 'line'
    if p.placement == 'Curved':
        d['text-placement'] = 'line'
    if p.placement == 'Horizontal':
        d['text-placement'] = 'interior'
    if p.placement == 'Free':
        d['text-placement'] = 'interior'

    d['text-face-name'] = 'string', p.fontFamily + ' ' + p.namedStyle
    d['text-fill'] = 'color', p.textColor

    if p.isExpression == '1':
        # this doesn't really work because QGIS syntax != postgres
        cc.error(error.EXPRESSION_NOT_SUPPORTED)
        d['text-name'] = 'string', ''
    else:
        d['text-name'] = 'field', p.fieldName

    if p.fontSizeInMapUnits == '1':
        d['text-size'] = 'fontsize', [p.fontSize, 'MapUnit']
    else:
        d['text-size'] = 'fontsize', [p.fontSize, 'px']

    # d['text-allow-overlap'] = 'int', 1

    if p.bufferDraw == '1':
        d['text-halo-radius'] = 'float', p.bufferSize
        d['text-halo-fill'] = 'color', p.bufferColor


def convert(cc, sla, fns):
    d = {}
    p = symbol_props(cc, sla)
    for f in fns.split(','):
        globals()['do_' + f.strip()](cc, p, d)
    return d
