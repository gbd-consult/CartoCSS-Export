"""Export controller."""

import error, result, css, project, debug


class Process:
    def __init__(self, prj):
        self._fns = {}
        self._errors = set()
        self._rules = []
        self._props = {}
        self._ds = {}
        self._prj = prj
        self._uid = 0

    def register_exporters(self, fns):
        self._fns = fns

    def run(self):
        self._meta = project.metadata(self, self._prj)
        self._rules = self.export(self._prj)
        self.enum_rules(self._rules)

        # debug.ppp(self._rules, maxdepth=999)

        self._ds = {}

        self.convert_expressions(self._rules)
        self.add_expressions(self._meta)

        css_text = css.indent(css.generate(self, self._rules))

        return result.ExportResult(self._meta, css_text, self._errors)

    def enum_rules(self, rules):
        for r in rules:
            if r:
                r.uid = self._uid

        self._uid += 1

        for r in rules:
            if r:
                self.enum_rules(getattr(r, 'sub', []))

    def add_expressions(self, meta):
        for lp in meta['Layer']:
            if 'Datasource' in lp and '_table' in lp['Datasource']:
                select = ['*']
                for k, expr_id in self._ds.items():
                    expr, la_id = k
                    if la_id == lp['_id']:
                        select.append('(\n%s\n)::int AS _e%d' % (expr.strip(), expr_id))
                lp['Datasource']['table'] = '(SELECT %s\nFROM %s) AS t' % (
                    ',\n\n'.join(select),
                    lp['Datasource']['_table']
                )
                del lp['Datasource']['_table']
                del lp['_id']

    def convert_expressions(self, rules, la=None):
        for r in rules:
            if getattr(r, 'expr', None):
                key = (r.expr, la.id())
                if key in self._ds:
                    expr_id = self._ds[key]
                else:
                    expr_id = len(self._ds)
                    self._ds[key] = expr_id
                r.expr = '_e%d=1' % expr_id
            self.convert_expressions(getattr(r, 'sub', []), getattr(r, 'layer', la))

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

    def rule(self, obj, typ, **kwargs):
        return Rule(obj, typ, **kwargs)

    def errors(self):
        return sorted(self._errors)


class Rule:
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
        self.comment = self.get_comment()

        for k, v in kwargs.items():
            setattr(self, k, v)
