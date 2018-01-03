from YAMLMacros.lib.extend import apply
from YAMLMacros.lib.syntax import rule as _rule

from YAMLMacros.lib.include import include_resource

import sublime
from os import path

def get_extensions(node, eval, arguments):
    return [
        include_resource(file_path)
        for file_path in sublime.find_resources('*.yaml')
        if path.dirname(file_path).endswith('Packages/JSCustom/extensions')
        and arguments.get(path.splitext(path.basename(file_path))[0], None)
    ]

get_extensions.raw = True
