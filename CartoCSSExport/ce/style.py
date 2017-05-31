"""Map Qgis style props to Carto."""

import debug
import error
import defs

Unit = ['', 'Pixel', 'MM']
LineStyle = ['solid', 'no', 'dash', 'dot', 'dash dot', 'dash dot dot']


class SymbolLayerProps:
    outline_style = LineStyle
    line_style = LineStyle
    outline_width = 0
    line_width = 0
    outline_width_unit = Unit
    size_unit = Unit
    line_width_unit = Unit
    size = 0
    outline_color = 0
    line_color = 0
    joinstyle = ['miter', 'bevel', 'round']
    offset = 0
    offset_unit = ['', 'Pixel', 'MM']
    color = 0
    capstyle = ['square', 'flat', 'round']
    name = ['arrow', 'circle']
    # @todo: implement with polygon-pattern-file
    style = ['solid', 'no']  # "horizontal","vertical","cross","b_diagonal","f_diagonal","diagonal_x","dense1..7

    fontFamily = ''
    fontSize = 0
    namedStyle = ''
    textColor = 0
    fieldName = ''
    placement = ['AroundPoint', 'Line', 'Curved', 'Horizontal', 'Free']


ResolveDefs = {
    'placement': 'Placement'

}


def symbol_props(cc, sla):
    p = SymbolLayerProps()

    for name, val in sla.properties().items():
        if not hasattr(p, name):
            cc.error(error.PROP_NOT_IMPLEMENTED, sla.layerType() + '.' + name)
            continue

        if name in ResolveDefs:
            val = getattr(defs, ResolveDefs[name])[int(val)]

        known_values = getattr(p, name)
        if isinstance(known_values, list) and val not in known_values:
            cc.error(error.VALUE_NOT_IMPLEMENTED, sla.layerType() + '.' + name + '=' + str(val))
            setattr(p, name, '')
            continue

        setattr(p, name, val)

    for name in dir(p):
        val = getattr(p, name)
        if isinstance(val, list):
            setattr(p, name, val[0])

    return p


def do_line_style(style, d):
    if style == 'dash':
        d['line-dasharray'] = 'list', [10, 4]
    if style == 'dot':
        d['line-dasharray'] = 'list', [4, 4]
    if style == 'dash dot':
        d['line-dasharray'] = 'list', [10, 4, 4, 4]
    if style == 'dash dot dot':
        d['line-dasharray'] = 'list', [10, 4, 4, 4, 4, 4]


def do_outline(p, d):
    if p.outline_style == 'no':
        return

    do_line_style(p.outline_style, d)

    d['line-width'] = 'size', [p.outline_width, p.outline_width_unit]
    d['line-color'] = 'color', p.outline_color

    if p.joinstyle:
        d['line-join'] = 'string', p.joinstyle


def do_fill(p, d):
    if p.style == 'no':
        return
    d['polygon-fill'] = 'color', p.color


def do_line(p, d):
    if p.line_style == 'no':
        return

    do_line_style(p.line_style, d)

    d['line-width'] = 'size', [p.line_width, p.line_width_unit]
    d['line-color'] = 'color', p.line_color

    if p.joinstyle:
        d['line-join'] = 'string', p.joinstyle

    if p.capstyle == 'flat':
        d['line-cap'] = 'string', 'butt'
    if p.capstyle in ('round', 'square'):
        d['line-cap'] = 'string', p.capstyle


def do_marker(p, d):
    d['marker-fill'] = 'color', p.color
    d['marker-width'] = 'size', [p.size, p.size_unit]
    d['marker-height'] = 'size', [p.size, p.size_unit]

    if p.name == 'circle':
        d['marker-type'] = 'string', 'ellipse'
    if p.name == 'arrow':
        d['marker-type'] = 'string', 'arrow'


def do_label(p, d):
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
    d['text-name'] = 'field', p.fieldName
    d['text-size'] = 'float', p.fontSize


def convert(cc, sla, fns):
    d = {}
    p = symbol_props(cc, sla)
    for f in fns.split(','):
        globals()['do_' + f.strip()](p, d)
    return d
