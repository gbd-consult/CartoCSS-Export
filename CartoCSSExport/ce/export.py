"""Export controller."""

import error, result, css, project, debug


class Process:
    def __init__(self, prj):
        self._fns = {}
        self._errors = set()
        self._rules = []
        self._props = {}
        self._exprs = {}
        self._meta = {}
        self._prj = prj
        self._uid = 0
        self._exprs = {}
        self._layer_stack = []

    def register_exporters(self, fns):
        self._fns = fns

    def run(self):
        self._meta = project.metadata(self, self._prj)
        self._rules = self.export(self._prj)
        self.insert_expressions(self._meta)
        css_text = css.indent(css.generate(self, self._rules))
        return result.ExportResult(self._meta, css_text, self._errors)

    def var(self, expr):
        la = self._layer_stack[-1]
        expr = expr.strip()
        if not expr:
            return ''
        key = (expr, la.id())
        if key not in self._exprs:
            self._exprs[key] = len(self._exprs)
        return '_e%d' % self._exprs[key]

    def insert_expressions(self, meta):
        for lp in meta['Layer']:
            if 'Datasource' in lp and '_orig_table' in lp['Datasource']:
                select = ['*']

                for k, expr_id in self._exprs.items():
                    expr, la_id = k
                    if la_id == lp['_orig_id']:
                        select.append('(%s)::int AS _e%d' % (expr, expr_id))

                lp['Datasource']['table'] = '(SELECT %s FROM %s) AS t' % (
                    ', '.join(select),
                    lp['Datasource']['_orig_table']
                )

    def error(self, msg, arg=''):
        self._errors.add((msg, unicode(arg)))

    def export(self, obj):
        if obj is None:
            raise ValueError

        cls = obj.__class__.__name__
        fn = self._fns.get(cls)
        if fn:
            return fn(self, obj)
        self.error(error.CLASS_NOT_IMPLEMENTED, cls)

    def enter_layer(self, la):
        self._layer_stack.append(la)

    def leave_layer(self):
        self._layer_stack.pop()

    def clause(self, obj, typ, **kwargs):
        return Clause(obj, typ, **kwargs)

    def errors(self):
        return sorted(self._errors)


class Clause:
    def get_comment(self):
        try:
            return self.obj.description()
        except:
            pass
        try:
            return self.obj.name()
        except:
            pass
        try:
            return self.obj.attributes['description']
        except:
            pass

    def __init__(self, obj, typ, **kwargs):
        self.typ = typ or obj.__class__.__name__
        self.obj = obj
        self.comment = kwargs.get('comment') or self.get_comment()
        for k, v in kwargs.items():
            setattr(self, k, v)
