"""CSS generator."""

import re
import value, expression

map_props = {
    'background-color': ['color', '#fff']
}


def indent(text, size=2):
    """Indent a css text."""

    def _indent(text):
        ii = 0
        for s in text.splitlines():
            s = s.strip()
            if not s:
                continue
            if s.endswith('}'):
                ii -= 1
            yield (' ' * (ii * size)) + s
            if s.endswith('{'):
                ii += 1

    return '\n'.join(_indent(text))


def _format_props(cc, plist):
    ps = []

    for name, val in plist.items():
        if isinstance(val, basestring):
            typ, v = 'string', val
        else:
            typ, v = plist[name]
        f, err, errval = value.format(typ, v)
        if err:
            cc.error(err, unicode(errval))
        if f is not None:
            ps.append('%s: %s;' % (name, f))

    return '\n'.join(ps)


def generate_rule(cc, rule):
    """Generate mss text from a ruleset."""

    if not rule:
        return ''

    if isinstance(rule, list):
        return '\n'.join(generate_rule(cc, r) for r in rule)

    sel = []

    if hasattr(rule, 'id'):
        sel.append('#' + rule.id)

    if getattr(rule, 'expr', ''):
        sel.append('[%s]' % rule.expr)

    if hasattr(rule, 'zoom'):
        sel.append(value.as_zoom(rule.zoom))

    subs = [s for s in getattr(rule, 'sub', []) if s]
    props = getattr(rule, 'props', {})

    if not sel:
        if not props and len(subs) < 2:
            return generate_rule(cc, subs)

    sel = ''.join(sel)

    if '#' not in sel:
        sel = '::' + rule.typ + '_' + str(rule.uid) + sel

    content = generate_rule(cc, subs) + '\n' + _format_props(cc, props)
    content = content.strip()

    if content:
        return sel + ' {\n' + content + '\n}\n'

    return ''


def generate(cc, rule):
    s = generate_rule(cc, rule)
    return 'Map {\n' + _format_props(cc, map_props) + '\n}\n' + s
