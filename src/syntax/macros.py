from yamlmacros.lib.extend import apply
from yamlmacros.lib.include import include_resource  # noqa: F401

from sublime_lib import ResourcePath


__all__ = ['apply', 'include_resource', 'get_extensions']


def get_extensions(path):
    arguments = (yield).context
    ret = []
    for file_path in ResourcePath.glob_resources(path):
        if arguments.get(file_path.stem) not in (None, False):
            ret.append((yield from include_resource(str(file_path))))

    return ret
