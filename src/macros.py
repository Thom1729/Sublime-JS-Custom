from yamlmacros.lib.extend import apply
from yamlmacros.lib.syntax import rule as _rule
from yamlmacros.lib.include import include_resource

from yamlmacros import process_macros

import sublime
from os import path


__all__ = ['apply', 'include_resource', 'get_extensions']


def merge(*args):
    ret = {}
    for arg in args:
        ret.update(arg)
    return ret

def has_value(val):
    return val is not None and val is not False

def get_extensions(node, eval, arguments):
    return [
        process_macros(
            sublime.load_resource(file_path),
            arguments=merge(arguments, { "file_path": file_path }),
        )
        for file_path in sublime.find_resources('*.yaml')
        if path.dirname(file_path).endswith('Packages/JSCustom/extensions')
        and has_value(arguments.get(path.splitext(path.basename(file_path))[0], None))
    ]

get_extensions.raw = True
