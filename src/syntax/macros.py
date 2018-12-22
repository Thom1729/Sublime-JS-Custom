from yamlmacros.lib.extend import apply

from yamlmacros import process_macros
from yamlmacros.src.util import merge
from yamlmacros.lib.include import include_resource  # noqa: F401

from sublime_lib import ResourcePath


__all__ = ['apply', 'include_resource', 'get_extensions']


def get_extensions(path):
    arguments = (yield).context
    return [
        process_macros(
            file_path.read_text(),
            arguments=merge(arguments, {"file_path": str(file_path)}),
        )
        for file_path in ResourcePath.glob_resources(path)
        if arguments.get(file_path.stem) not in (None, False)
    ]
