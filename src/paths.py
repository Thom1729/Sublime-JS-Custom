import sublime

from os import path

TEST_PATH = 'User/JS Custom/Tests'
SOURCE_PATH = 'Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros'

def resource_path(*parts):
    return path.join('Packages', *parts)

def system_path(*parts):
    return path.join(sublime.packages_path(), *parts)
