from sublime_lib import ResourcePath

import shutil

TEST_PATH = ResourcePath('Packages/User/JS Custom/Tests')
USER_DATA_PATH = ResourcePath('Packages/User/JS Custom/')
SOURCE_PATH = ResourcePath('Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros')


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
    shutil.rmtree(str(ResourcePath('Packages/User/JS Custom').file_path()))


def tests_system_path():
    return TEST_PATH.file_path()


def clean_tests():
    if tests_system_path().exists():
        shutil.rmtree(str(tests_system_path()))
    tests_system_path().mkdir(parents=True)
