import sys
from uuid import uuid4

import importlib
from importlib.abc import MetaPathFinder, SourceLoader

from sublime_lib import ResourcePath

__all__ = ['TemporaryPackageFinder']


class TemporaryFileLoader(SourceLoader):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def get_filename(self, fullname):
        return str(self.path)

    def get_data(self, path):
        return ResourcePath(path).read_bytes()

    def module_repr(self, module):
        return "module_repr()"


class TemporaryPackageFinder(MetaPathFinder):
    def __init__(self, path, name = None, *, prefix = None, suffix = None):
        self.path = path
        if name is None:
            self._name = '{prefix}{token}{suffix}'.format(
                prefix=prefix or '',
                token=uuid4(),
                suffix=suffix or '',
            )
        elif prefix is not None or suffix is not None:
            raise ValueError("Argument `name` is incompatible with `prefix` and `suffix`.")
        else:
            self._name = name

    def is_mine(self, fullname):
        return fullname == self._name or fullname.startswith(self._name + '.')

    def find_loader(self, fullname, path):
        if self.is_mine(fullname):
            print('FINDER', fullname, path)

            parts = fullname.split('.')[1:]

            base_path = self.path.joinpath(*parts)
            init_path = base_path / '__init__.py'
            file_path = base_path.with_suffix('.py')

            portion = [
                base_path.file_path()
            ]
            
            if init_path.exists():
                return (TemporaryFileLoader(fullname, init_path), portion)
            elif file_path.exists():
                return (TemporaryFileLoader(fullname, file_path), portion)
            else:
                return (None, portion)
        else:
            return (None, [])

    def find_module(self, fullname, path):
        return self.find_loader(fullname, path)[0]

    def __enter__(self):
        sys.meta_path.append(self)
        return importlib.import_module(self._name)

    def __exit__(self, *args):
        try:
            sys.meta_path.remove(self)
        except ValueError:
            pass

        modules = [
            name
            for name in sys.modules
            if self.is_mine(name)
        ]
        for name in modules:
            # print("Removing", name)
            sys.modules.pop(name)
