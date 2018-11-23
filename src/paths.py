import sublime

from sublime_lib import ResourcePath

import os
from os import path
import shutil

TEST_PATH = ResourcePath('Packages/User/JS Custom/Tests')
SOURCE_PATH = ResourcePath('Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros')


def resource_path(*parts):
    return path.join('Packages', *parts)


def system_path(*parts):
    return path.join(sublime.packages_path(), *parts)


def compiled_syntaxes_system_path():
    return ResourcePath('Packages/User/JS Custom/Syntaxes').file_path()


def clean_syntaxes(keep=set()):
    directory_path = ResourcePath('Packages/User/JS Custom/Syntaxes').file_path()

    if directory_path.exists():
        for filename in directory_path.iterdir():
            if filename.suffix == '.sublime-syntax' and filename.name not in keep:
                (directory_path / filename).unlink()
    else:
        directory_path.mkdir(parents=True)


def clear_user_data():
    shutil.rmtree(system_path('User', 'JS Custom'))


def tests_system_path():
    return TEST_PATH.file_path()


def clean_tests():
    if tests_system_path().exists():
        shutil.rmtree(str(tests_system_path()))
    os.makedirs(str(tests_system_path()))
