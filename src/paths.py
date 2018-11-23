from sublime_lib import ResourcePath

import shutil

USER_DATA_PATH = ResourcePath('Packages/User/JS Custom')
PACKAGE_PATH = ResourcePath('Packages/JSCustom')
# SOURCE_PATH = ResourcePath('Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros')
SOURCE_PATH = PACKAGE_PATH / 'src/syntax/JS Custom.sublime-syntax.yaml-macros'


def clean_syntaxes(keep=set()):
    for syntax_path in USER_DATA_PATH.glob('Syntaxes/*.sublime-syntax'):
        if syntax_path.name not in keep:
            syntax_path.file_path().unlink()

    try:
        (USER_DATA_PATH / 'Syntaxes').file_path().mkdir(parents=True)
    except FileExistsError:
        pass


def clear_user_data():
    shutil.rmtree(str(USER_DATA_PATH.file_path()))


def clean_tests():
    p = (USER_DATA_PATH / 'Tests').file_path()

    try:
        shutil.rmtree(str(p))
    except FileNotFoundError:
        pass

    p.mkdir(parents=True)
