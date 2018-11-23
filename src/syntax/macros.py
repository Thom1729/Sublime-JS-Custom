from yamlmacros.lib.extend import apply

from yamlmacros import process_macros
from yamlmacros.src.util import merge
from yamlmacros.lib.include import include_resource

import sublime
from os import path


def _include_resource(file_path, loader):
    file_contents = sublime.load_resource(file_path)
    return process_macros(
        file_contents,
        arguments=merge(loader.context, { "file_path": file_path }),
    )


def has_value(val):
    return val is not None and val is not False


def get_extensions(node, loader):
    return [
        _include_resource(file_path, loader)
        for file_path in sublime.find_resources('*.yaml')
        if path.dirname(file_path).endswith('Packages/JSCustom/extensions')
        and has_value(loader.context.get(path.splitext(path.basename(file_path))[0], None))
    ]

get_extensions.raw = True
