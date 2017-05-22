"""Converters for Qgs Renderers."""


def exportQgsSingleSymbolRendererV2(cc, rnd):
    sub = [cc.export(sym) for sym in rnd.symbols()]
    return cc.rule('SingleSymbolRenderer', sub=sub)


def exportQgsRuleBasedRendererV2(cc, rnd):
    sub = [cc.export(rnd.rootRule())]
    return cc.rule('RuleBasedRenderer', sub=sub)


def exportRule(cc, rule):
    if not rule.active():
        return None

    sub = []

    if rule.symbol():
        sub.append(cc.export(rule.symbol()))

    ch = [cc.export(r) for r in rule.children()]
    sub.extend(ch)

    r = cc.rule('RendererRule', label=rule.label(), expr=rule.filterExpression(), sub=sub)

    if rule.dependsOnScale():
        r.zoom = [rule.scaleMaxDenom(), rule.scaleMinDenom()]

    return r


def exportQgsCategorizedSymbolRendererV2(cc, rnd):
    sub = []
    attr = rnd.classAttribute()

    for cat in rnd.categories():
        p = cc.export(cat.symbol())
        val = cat.value()
        sub.append(cc.rule('RenderCategory', attr=attr, value=val, sub=[p]))

    return cc.rule('CategorizedSymbolRenderer', sub=sub)
