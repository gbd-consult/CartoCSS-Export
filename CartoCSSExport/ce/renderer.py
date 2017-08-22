"""Converters for Qgs Renderers."""

import debug


def exportQgsSingleSymbolRendererV2(cc, rnd):
    sub = [cc.export(sym) for sym in rnd.symbols()]
    return cc.clause(rnd, 'SingleSymbolRenderer', sub=sub)


def exportQgsRuleBasedRendererV2(cc, rnd):
    sub = [cc.export(rnd.rootRule())]
    return cc.clause(rnd, 'RuleBasedRenderer', sub=sub)


def exportRule(cc, rule):
    if not rule.active():
        return None

    sub = []

    if rule.symbol():
        sub.append(cc.export(rule.symbol()))

    ch = [cc.export(r) for r in rule.children()]
    sub.extend(ch)

    r = cc.clause(
        rule,
        'RendererRule',
        comment='%s: %s' % (rule.label(),rule.filterExpression()),
        filter=cc.var(rule.filterExpression()),
        sub=sub)

    if rule.dependsOnScale():
        r.zoom = [rule.scaleMaxDenom(), rule.scaleMinDenom()]

    return r


def _equals(attr, val):
    return "%s='%s'" % (attr, val)


def exportQgsCategorizedSymbolRendererV2(cc, rnd):
    sub = []
    attr = rnd.classAttribute()

    for cat in rnd.categories():
        p = cc.export(cat.symbol())
        val = cat.value()
        sub.append(cc.clause(
            cat,
            'RenderCategory',
            comment='%s=%s' % (attr, val),
            filter=cc.var(_equals(attr, val)),
            sub=[p]
        ))

    return cc.clause(rnd, 'CategorizedSymbolRenderer', sub=sub)
