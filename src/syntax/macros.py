import sublime
import importlib

from yamlmacros.lib.extend import apply
from yamlmacros.lib.include import include_resource  # noqa: F401

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


def find_extensions(path):
    for about_path in ResourcePath.glob_resources('*.syntax-extension'):
        about = sublime.decode_value(about_path.read_text())
        about.setdefault('name', about_path.stem)
        about.setdefault('module', '.')
        about.setdefault('path', about_path)
        yield about


def load_extension_functions(name, path):
    ret = {
        'get_options': lambda options: options,
    }

    with TemporaryPackageFinder(path, prefix='JSCustom_extension') as package:
        module = importlib.import_module(name, package.__name__)
        return {
            'get_options': getattr(module, 'get_options', lambda options: options)
        }

def get_newfangled_extensions(path):
    arguments = (yield).context
    ret = []

    for about in find_extensions(path):
        name = about['name']
        about_path = about['path']
        module_name = about['module']

        options = arguments.get(name)
        if options is not None and options is not False:
            print('EXTENSION', name)

            extension_functions = load_extension_functions(module_name, about_path.parent)
            extension_path = about_path.parent / about.get('extension', 'extension.yaml')

            with (yield extension_functions['get_options'](options)):
                ret.append((yield from include_resource(str(extension_path))))

    return ret
