from yamlmacros.lib.extend import apply
from yamlmacros.lib.syntax import rule as _rule

from yamlmacros import process_macros

import sublime
from os import path

def include_resource(resource):
    file_contents = sublime.load_resource(resource)
    return process_macros(
        file_contents,
        arguments={ "file_path": resource },
    )


def get_extensions(node, eval, arguments):
    return [
        include_resource(file_path)
        for file_path in sublime.find_resources('*.yaml')
        if path.dirname(file_path).endswith('Packages/JSCustom/extensions')
        and arguments.get(path.splitext(path.basename(file_path))[0], None)
    ]

get_extensions.raw = True
