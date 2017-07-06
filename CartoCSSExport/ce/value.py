"""Format CartoCSS values."""

import re
import error


def as_string(val):
    return "'%s'" % unicode(val).strip().replace("'", "\\'")


mm_per_inch = 25.4
default_ppi = 90


def to_float_with_comma(s):
    try:
        return float(s)
    except ValueError:
        pass

    return float(s.replace(',', '.'))


# @todo: this is an arbitrary value
PX_IN_MAP_UNIT = 10


def as_size(val):
    v, unit = val

    v = to_float_with_comma(v)
    unit = unit.lower()

    if unit == 'mapunit':
        return PX_IN_MAP_UNIT, error.UNIT_NOT_IMPLEMENTED, unit
    if unit == 'mm':
        v = round((v / mm_per_inch) * default_ppi)
    elif unit in ('pixel', 'px'):
        v = round(v)
    else:
        return round(v), error.UNIT_NOT_IMPLEMENTED, unit

    return str(int(v))


def as_float(val):
    if isinstance(val, (int, float)):
        return '%s' % val

    if isinstance(val, basestring):
        try:
            return '%s' % int(val)
        except ValueError:
            pass
        try:
            return '%s' % to_float_with_comma(val)
        except ValueError:
            pass

    return None, error.INVALID_NUMBER, val


def as_color(val):
    # string r,g,b,a
    if isinstance(val, basestring):
        if re.match(r'^(\d+,\s*){3}\d+$', val):
            return 'rgba(%s)' % val
        if re.match(r'^(\d+,\s*){2}\d+$', val):
            return 'rgba(%s,255)' % val

    # list [r,g,b,a]
    if isinstance(val, (list, tuple)):
        return 'rgba(%d,%d,%d,%d)' % tuple(map(int, val))

    # QtGui.QColor
    if hasattr(val, 'alpha'):
        return 'rgba(%d,%d,%d,%d)' % (
            val.red(),
            val.green(),
            val.blue(),
            val.alpha()
        )

    # number
    if isinstance(val, (float, int)):
        return '#%06x' % int(val)

    return None, error.INVALID_COLOR, val


def as_field(val):
    m = re.match(r'^\w+$', val)
    if m:
        return '[%s]' % val
    return None, error.INVALID_FIELD, val


def as_list(val):
    return ', '.join(map(unicode, val))


# from https://github.com/mapbox/carto/blob/master/lib/carto/tree/zoom.js

CartoZoomRanges = {
    0: 1000000000,
    1: 500000000,
    2: 200000000,
    3: 100000000,
    4: 50000000,
    5: 25000000,
    6: 12500000,
    7: 6500000,
    8: 3000000,
    9: 1500000,
    10: 750000,
    11: 400000,
    12: 200000,
    13: 100000,
    14: 50000,
    15: 25000,
    16: 12500,
    17: 5000,
    18: 2500,
    19: 1500,
    20: 750,
    21: 500,
    22: 250,
    # 23: 100
}


def as_zoom(val):
    def scale_to_level(scale):
        for l, s in sorted(CartoZoomRanges.items()):
            if scale == s:
                return l, l
            if scale > s:
                return max(0, l - 1), l
        return 22, 22

    qmin, qmax = map(int, val)

    a1, a2 = scale_to_level(max(qmin, qmax))
    z1, z2 = scale_to_level(min(qmin, qmax))

    ao = '>=' if a1 == a2 else '>'
    zo = '<=' if z1 == z2 else '<'

    a = min(a1, a2)
    z = max(z1, z2)

    if a == z:
        return '[zoom=%d]' % a

    return '[zoom%s%d][zoom%s%d]' % (ao, a, zo, z)


def format(typ, val):
    fn = globals().get('as_' + typ)
    res = fn(val)
    if isinstance(res, tuple):
        return res
    return res, None, None
