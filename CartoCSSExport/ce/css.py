"""CSS generator."""

import re
import debug, value, expression

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


def generate_clause(cc, clause):
    """Generate mss text from a set of style clauses."""

    if not clause:
        return ''

    if isinstance(clause, list):
        return '\n'.join(generate_clause(cc, r) for r in clause)

    sel = []

    if hasattr(clause, 'id'):
        sel.append('#' + clause.id)

    if getattr(clause, 'filter', ''):
        sel.append('[%s=1]' % clause.filter)

    if hasattr(clause, 'zoom'):
        sel.append(value.as_zoom(clause.zoom))

    subs = [s for s in getattr(clause, 'sub', []) if s]
    props = getattr(clause, 'props', {})

    if not sel:
        if not props and len(subs) < 2:
            return generate_clause(cc, subs)

    sel = ''.join(sel)

    if '#' not in sel:
        sel = '::' + clause.typ + '_' + str(_uid()) + sel

    content = generate_clause(cc, subs) + '\n' + _format_props(cc, props)
    content = content.strip()

    if content:
        content = sel + ' {\n' + content + '\n}\n'
        if clause.comment:
            s = clause.comment.strip()
            s = re.sub(r'\s+', ' ', s.replace('*', ' '))
            content = '/* ' + s + ' */\n' + content
        return content

    return ''


def generate(cc, clause):
    s = generate_clause(cc, clause)
    return 'Map {\n' + _format_props(cc, map_props) + '\n}\n' + s
