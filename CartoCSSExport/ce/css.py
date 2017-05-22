"""CSS generator."""

import re
import value, expression


def indent(text):
    """Indent a css text."""

    def _indent(text):
        ii = 0
        for s in text.splitlines():
            s = s.strip()
            if not s:
                continue
            if s.endswith('}'):
                ii -= 1
            yield (' ' * (ii * 4)) + s
            if s.endswith('{'):
                ii += 1

    return '\n'.join(_indent(text))


def generate(cc, rule):
    """Generate mss text from a ruleset."""

    def fprops(p):
        ps = []

        for name, val in p.items():
            if isinstance(val, basestring):
                typ, v = 'string', val
            else:
                typ, v = p[name]
            f, err = value.format(typ, v)
            if err:
                cc.error(err, unicode(val))
                continue
            ps.append('%s: %s;' % (name, f))

        return '\n'.join(ps)

    if not rule:
        return ''

    if isinstance(rule, list):
        return '\n'.join(generate(cc, r) for r in rule)

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
            return generate(cc, subs)

    sel = ''.join(sel)

    if '#' not in sel:
        sel = '::' + rule.typ + '_' + str(rule.uid) + sel

    content = (generate(cc, subs) + '\n' + fprops(props)).strip()

    if content:
        return sel + ' {\n' + content + '\n}\n'

    return ''
