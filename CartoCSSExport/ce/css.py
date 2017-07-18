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
            val = 'string', val
        f, err, errval = value.format(*val)
        if err:
            cc.error(err, unicode(errval))
        if isinstance(f, (list, tuple)):
            for sel, v in f:
                ps.append('[%s] { %s: %s }' % (sel, name, v))
        elif f is not None:
            ps.append('%s: %s;' % (name, f))

    return '\n'.join(ps)


__uid = 0


def _uid():
    global __uid
    __uid += 1
    return __uid


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
        # sel = '::' + rule.typ + '_' + str(rule.uid) + sel
        sel = '::' + rule.typ + '_' + str(_uid()) + sel

    content = generate_rule(cc, subs) + '\n' + _format_props(cc, props)
    content = content.strip()

    if content:
        content = sel + ' {\n' + content + '\n}\n'
        if rule.comment:
            content = '/* ' + rule.comment + ' */\n' + content
        return content

    return ''


def generate(cc, rule):
    s = generate_rule(cc, rule)
    return 'Map {\n' + _format_props(cc, map_props) + '\n}\n' + s
