from YAMLMacros.lib.extend import *

def get(key):
    global _context
    return _context[key]

from YAMLMacros.src.build import _build_yaml_macros

def _include(name):
    global _context
    with open(name, 'r') as file:
        return _build_yaml_macros(
            file.read(), _context
        )

def apply_all(base, *extensions):
    ret = _include(base)
    for extension in extensions:
        ret = Merge(_include(extension)).apply(ret)

    return ret