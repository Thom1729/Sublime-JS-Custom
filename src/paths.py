import sublime

import os
from os import path
import shutil

TEST_PATH = 'User/JS Custom/Tests'
SOURCE_PATH = 'Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros'



def resource_path(*parts):
    return path.join('Packages', *parts)

def system_path(*parts):
    return path.join(sublime.packages_path(), *parts)



def compiled_syntaxes_system_path():
    return system_path('User', 'JS Custom', 'Syntaxes')

def clean_syntaxes(keep=set()):
    directory_path = compiled_syntaxes_system_path()

    if path.exists(directory_path):
        for filename in os.listdir(directory_path):
            name, ext = path.splitext(filename)
            if ext == '.sublime-syntax' and name not in keep:
                os.remove(path.join(directory_path, filename))
    else:
        os.makedirs(directory_path)

def clear_user_data():
    shutil.rmtree(system_path('User', 'JS Custom'))

def tests_system_path():
    return system_path(TEST_PATH)

def clean_tests():
    if path.exists(tests_system_path()):
        shutil.rmtree(tests_system_path())
    os.makedirs(tests_system_path())
