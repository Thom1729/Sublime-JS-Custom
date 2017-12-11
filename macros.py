from YAMLMacros.lib.extend import *
from YAMLMacros.lib.arguments import *

from YAMLMacros.lib.extend import Operation

import re

def find_rule(condition, node, parent=None):
    if isinstance(node, list):
        for item in node: yield from find_rule(condition, item, node)
    elif isinstance(node, dict):
        if condition(node):
            yield (parent, node)
        else:
            for key, item in node.items():
                yield from find_rule(condition, item, node)

class StripJquery(Operation):
    def apply(self, base):
        rules = list(find_rule(
            lambda node: 'dollar' in node.get('scope', ''),
            base
        ))

        for parent, node in rules:
            parent.remove(node)

        return base

class HighlightDollarIdentifiers(Operation):
    def apply(self, base):
        rules = list(find_rule(
            lambda node: node.get('match', '') == '{{identifier}}',
            base
        ))

        # print(rules)

        for parent, node in rules:
            node['match'] = r'({{dollar_only_identifier}})|({{dollar_identifier}})|({{identifier}})'
            scope = node['scope']
            del node['scope']
            node['captures'] = {
                1: re.sub(r'(\.readwrite)?\.js', '.dollar.only.js', scope, 1) + ' punctuation.dollar.js',
                2: re.sub(r'(\.readwrite)?\.js', '.dollar.js', scope, 1),
                3: 'punctuation.dollar.js',
                4: scope,
            }

        return base

def strip_jquery(*args):
    return StripJquery(None)

def highlight_dollar_identifiers(*args):
    return HighlightDollarIdentifiers(None)