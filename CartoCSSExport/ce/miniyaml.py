"""Minimal yaml dumper."""


def _to_string(t):
    return unicode(t).encode('utf8', 'replace')


def _quote(t):
    t = t.replace('"', '\\"')
    t = t.replace('\n', '\\n')
    return '"' + t + '"'


def _is_ident(t):
    s = t.replace('_', '')
    return t and (not s or s.isalnum())


def _dump_dict(t):
    keys = sorted(
        (_to_string(k) for k in t),
        key=lambda k: k.upper().replace('_', ' '))

    if 'id' in keys:
        keys.remove('id')
        keys = ['id'] + keys

    for k in keys:
        ks = k if _is_ident(k) else _quote(k)
        sub = _dump(t[k])
        if isinstance(sub, list):
            yield ks + ':'
            for x in sub:
                yield '  ' + x
        else:
            yield ks + ': ' + sub


def _dump_list(t):
    for v in t:
        sub = _dump(v)
        if isinstance(sub, list):
            yield '- ' + sub[0]
            for x in sub[1:]:
                yield '  ' + x
        else:
            yield '- ' + sub


def _dump(t):
    if isinstance(t, dict):
        return list(_dump_dict(t))

    if isinstance(t, (list, tuple)):
        if not t:
            return '[]'
        return list(_dump_list(t))

    if isinstance(t, bool):
        return 'true' if t else 'false'

    if isinstance(t, (int, float)):
        return str(t)

    if isinstance(t, basestring):
        t = t.replace('\r\n', '\n').strip()

        if not t:
            return "''"

        t = _to_string(t)
        return _quote(t) if any(x in t for x in ':\n\'\"') else t

    raise ValueError('Object of type %s is not serializable' % type(t))


def dump(t):
    return '\n'.join(_dump(t)) + '\n'
