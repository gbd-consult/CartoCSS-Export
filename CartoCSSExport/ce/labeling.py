"""Converters for Qgis Labeling."""

import re
import defs
import debug
import style


def normalize_props(props):
    if not props:
        return None

    # simple lables use separate R,G,B,A fields, rules use 4-tuples
    colors = 'buffer', 'text', 'shadow', 'shapeFill', 'shapeBorder'
    for c in colors:
        if c + 'ColorR' in props:
            props[c + 'Color'] = ','.join([
                props.pop(c + 'ColorR', '0'),
                props.pop(c + 'ColorG', '0'),
                props.pop(c + 'ColorB', '0'),
                props.pop(c + 'ColorA', '255')
            ])

    # simples use 'true/false', rules use '1/0'
    for k in props:
        if props[k] == 'true':
            props[k] = '1'
        if props[k] == 'false':
            props[k] = '0'

    # these are only used for simples
    props.pop('drawLabels', None)
    props.pop('enabled', None)

    return {k:v for k, v in props.items() if k not in defs.LabelDefaults or v != defs.LabelDefaults[k]}


class CeLabelingSymbolLayer:
    # must support layerType and properties

    def properties(self):
        return self.props


class CeSimpleLabeling(CeLabelingSymbolLayer):
    def __init__(self, props):
        self.props = normalize_props(props)

    def layerType(self):
        return 'SimpleLabeling'


def exportCeSimpleLabeling(cc, lab):
    props = style.convert(cc, lab, 'label')
    return cc.rule(lab.layerType(), props=props)


class CeRuleBasedLabeling(CeLabelingSymbolLayer):
    def __init__(self, rules):
        self.sub = rules

    def layerType(self):
        return 'RuleLabeling'


def exportCeRuleBasedLabeling(cc, lab):
    return cc.rule('', sub=[cc.export(r) for r in lab.sub])


class CeRuleBasedLabelingRule(CeLabelingSymbolLayer):
    def __init__(self, attributes, props, sub):
        self.attributes = attributes
        self.props = normalize_props(props)
        self.sub = sub

    def layerType(self):
        return 'LabelingRule'


def exportCeRuleBasedLabelingRule(cc, lab):
    r = cc.rule(lab.layerType(), sub=[cc.export(r) for r in lab.sub])

    if 'scalemaxdenom' in lab.attributes:
        r.zoom = [lab.attributes['scalemindenom'], lab.attributes['scalemaxdenom']]

    if 'filter' in lab.attributes:
        r.expr = lab.attributes['filter']

    if lab.props:
        r.props = style.convert(cc, lab, 'label')
    return r


def rule_labeling_props(rule):
    # Although rule-based props are split into nodes (text-stype, shadow etc)
    # their attribute names appear to be unique,
    # so clump them together into one style object, just like for the simple labeling

    d = {}
    for c in rule['children']:
        if c['name'] == 'settings':
            for p in c['children']:
                d.update(p['attributes'])
    return d


def rule_labeling_rules(lbl_node):
    rules = []
    for c in lbl_node['children']:
        if c['name'] == 'rules':
            rules.extend(rule_labeling_rules(c))
        if c['name'] == 'rule':
            rules.append(CeRuleBasedLabelingRule(
                c['attributes'],
                rule_labeling_props(c),
                rule_labeling_rules(c)
            ))
    return rules


def simple_labeling_props(xd):
    # simple labeling props are stored in customproperties/labelingxxx

    d = {}

    for c in xd['children']:
        if c['name'] == 'customproperties':
            for p in c['children']:
                m = re.match(r'^labeling/(\w+)$', p['attributes'].get('key', ''))
                if m:
                    d[m.group(1)] = p['attributes'].get('value')

    return d


def from_layer_dict(xd):
    for c in xd['children']:
        if c['name'] == 'labeling':
            if c['attributes'].get('type') == 'simple':
                lp = simple_labeling_props(xd)
                if lp.get('enabled') != 'true':
                    return None
                return CeSimpleLabeling(lp)

            if c['attributes'].get('type') == 'rule-based':
                return CeRuleBasedLabeling(rule_labeling_rules(c))

            break
