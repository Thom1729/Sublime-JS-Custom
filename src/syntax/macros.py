import sublime
import importlib

from yamlmacros.lib.extend import apply
from yamlmacros.lib.include import include_resource  # noqa: F401
from yamlmacros import get_loader

from sublime_lib import ResourcePath


from JSCustom.src.temporary_package import TemporaryPackageFinder


__all__ = ['apply', 'include_resource', 'get_extensions', 'get_newfangled_extensions']


def get_extensions(path):
    arguments = (yield).context
    ret = []
    for file_path in ResourcePath.glob_resources(path):
        if arguments.get(file_path.stem) not in (None, False):
            ret.append((yield from include_resource(str(file_path))))

    return ret


def get_newfangled_extensions(path):
    arguments = (yield).context
    ret = []

    for path in ResourcePath.glob_resources('*.syntax-extension'):
        name = path.stem
        options = arguments.get(name)

        if options is not None and options is not False:

            yaml = get_loader(macros_root=str(path.parent))
            documents = yaml.load_all(path.read_text())

            metadata = next(documents)

            def get_options(options):
                if isinstance(options, dict):
                    return options
                else:
                    return {}

            with (yield).set_context(**get_options(options)):
                result = next(documents)
                ret.append(result)

    return ret
