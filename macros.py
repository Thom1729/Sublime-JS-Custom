from YAMLMacros.lib.extend import *
from YAMLMacros.src.build import _build_yaml_macros

from YAMLMacros.lib.context import setting, _get_context_stack

def option(key):
    return setting(key)

def if_(value, ifTrue, ifFalse=None):
    if value:
        return ifTrue
    else:
        return ifFalse

def include(name):
    with open(name, 'r') as file:
        return _build_yaml_macros(file.read())
