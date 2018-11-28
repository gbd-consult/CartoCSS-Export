"""CSS generator."""

import re
import debug, value, error, cartocss

map_props = {
    'background-color': ['color', '#fff']
}


def _merge(*args):
    d = {}
    for a in args:
        d.update(a or {})
    return d


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

        prop = cartocss.Properties.get(name)
        if not prop:
            cc.error(error.INVALID_CSS_PROP, name)
            continue

        if prop['type'] == 'keyword':
            val = ('keyword',) + val[1:]

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


def generate_clause(cc, clause, parent_props):
    """Generate mss text from a set of style clauses."""

    if not clause:
        return ''

    if isinstance(clause, list):
        return '\n'.join(generate_clause(cc, r, parent_props) for r in clause)

    sel = []

    if hasattr(clause, 'id'):
        sel.append('#' + clause.id)

    if getattr(clause, 'filter', ''):
        # removed complex expressions
        # sel.append('[%s=1]' % clause.filter)
        sel.append('[%s]' % clause.filter)

    if hasattr(clause, 'zoom'):
        sel.append(value.as_zoom(clause.zoom))

    subs = [s for s in getattr(clause, 'sub', []) if s]
    props = getattr(clause, 'props', {})

    if not sel:
        if not props and len(subs) < 2:
            return generate_clause(cc, subs, parent_props)

    sel = ''.join(sel)

    if '#' not in sel:
        sel = '::' + clause.typ + '_' + str(_uid()) + sel

    props = _merge(parent_props, props)

    if subs:
        content = generate_clause(cc, subs, props)
    else:
        content = _format_props(cc, props)

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
    s = generate_clause(cc, clause, {})
    return 'Map {\n' + _format_props(cc, map_props) + '\n}\n' + s
