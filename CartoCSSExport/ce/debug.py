"""Debuggging tools."""

import re
import collections


def inspect(arg, maxdepth=None, all=False):
    """Inspect the argument upto the given depth."""

    def dump(x, name=None, d=0):
        pfx = '    ' * d

        if name:
            pfx += str(name) + ': '

        t = str(type(x))
        m = re.match(r"^<(type|class) '(.+?)'>", t)
        pfx += m.group(2) if m else t

        try:
            pfx += '(%d)' % len(x)
        except:
            pass

        if x is None or isinstance(x, (bool, int, float, basestring)):
            yield pfx + ' = ' + repr(x)
            return

        if d >= maxdepth:
            yield pfx + '...'
            return

        if isinstance(x, collections.Mapping) and x:
            yield pfx + ' ='
            for k, v in x.iteritems():
                for s in dump(v, '{%s}' % k, d + 1):
                    yield s

        elif isinstance(x, (collections.Set, collections.Sequence)) and x:
            yield pfx + ' ='
            for k, v in enumerate(x):
                for s in dump(v, '[%s]' % k, d + 1):
                    yield s

        else:
            yield pfx + ' = ' + repr(x)

        for k in dir(x):
            try:
                v = getattr(x, k)
            except AttributeError:
                v = '?AttributeError'
            if all or (not k.startswith('__') and not callable(v)):
                for s in dump(v, k, d + 1):
                    yield s

    if maxdepth is None:
        maxdepth = 1 if all else 3

    for s in dump(arg):
        yield s


def pp(*args):
    for a in args:
        for s in inspect(a):
            print(s)
        print('-' * 16)


def ppp(arg, maxdepth=None, all=None):
    for s in inspect(arg, maxdepth, all):
        print(s)
