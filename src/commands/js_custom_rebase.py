import sublime_plugin
from sublime_lib import ResourcePath

from ..paths import PACKAGE_PATH


CORE_JAVASCRIPT_PATH = ResourcePath('Packages/JavaScript')
SYNTAX_TEST_PREFIX = 'syntax_test_'

__all__ = ['JsCustomRebaseCommand']


def copy(source, dest):
    source_path = source
    dest_path = dest.file_path()

    print("JS Custom: Copying {} to {}…".format(source_path, dest_path))
    source_path.copy(dest_path)


class JsCustomRebaseCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        copy(CORE_JAVASCRIPT_PATH / 'JavaScript.sublime-syntax', PACKAGE_PATH / 'src/syntax/JavaScript.yaml')
        copy(CORE_JAVASCRIPT_PATH / 'TypeScript.sublime-syntax', PACKAGE_PATH / 'extensions/typescript.syntax-extension')
        copy(CORE_JAVASCRIPT_PATH / 'JSX.sublime-syntax', PACKAGE_PATH / 'extensions/jsx.syntax-extension')

        for test in (CORE_JAVASCRIPT_PATH / 'tests').children():
            if test.stem.startswith(SYNTAX_TEST_PREFIX):
                suite = test.stem[len(SYNTAX_TEST_PREFIX):].split('_')[0]
                destination_name = test.name[len(SYNTAX_TEST_PREFIX):]
            else:
                print("Warning: could not determine suite for test {}.".format(test))

            copy(test, PACKAGE_PATH / 'tests/syntax_test_suites' / suite / destination_name)
