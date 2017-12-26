from YAMLMacros.lib.extend import *
from YAMLMacros.lib.arguments import *
from YAMLMacros.lib.syntax import *

from YAMLMacros.lib.include import include_resource

from YAMLMacros.lib.extend import Operation

from YAMLMacros.api import apply as _apply

# import re
import sublime
from os import path

def get_extensions(node, eval, arguments):
    return [
        include_resource(file_path)
        for file_path in sublime.find_resources('*.yaml')
        if path.dirname(file_path).endswith('/JSCustom/extensions')
        and arguments.get(path.splitext(path.basename(file_path))[0], None)
    ]

get_extensions.raw = True

# def find_rule(condition, node, parent=None):
#     if isinstance(node, list):
#         for item in node: yield from find_rule(condition, item, node)
#     elif isinstance(node, dict):
#         if condition(node):
#             yield (parent, node)
#         else:
#             for key, item in node.items():
#                 yield from find_rule(condition, item, node)

# class StripJquery(Operation):
#     def apply(self, base):
#         rules = list(find_rule(
#             lambda node: 'dollar' in node.get('scope', ''),
#             base
#         ))

#         for parent, node in rules:
#             parent.remove(node)

#         return base

# class HighlightDollarIdentifiers(Operation):
#     def apply(self, base):
#         rules = list(find_rule(
#             lambda node: node.get('match', '') == '{{identifier}}',
#             base
#         ))

#         # print(rules)

#         for parent, node in rules:
#             node['match'] = r'({{dollar_only_identifier}})|({{dollar_identifier}})|({{identifier}})'
#             scope = node['scope']
#             del node['scope']
#             node['captures'] = {
#                 1: re.sub(r'(\.readwrite)?\.js', '.dollar.only.js', scope, 1) + ' punctuation.dollar.js',
#                 2: re.sub(r'(\.readwrite)?\.js', '.dollar.js', scope, 1),
#                 3: 'punctuation.dollar.js',
#                 4: scope,
#             }

#         return base

# def strip_jquery(*args):
#     return StripJquery(None)

# def highlight_dollar_identifiers(*args):
#     return HighlightDollarIdentifiers(None)

def expect_identifier(scope):
    return [
        rule(
            match=r'{{identifier}}',
            scope=scope,
            pop=True
        ),
        rule(include='else-pop'),
    ]
