import sublime_plugin
from sublime_lib import ResourcePath

from JSCustom.src.paths import PACKAGE_PATH


__all__ = ['UpdateJsCustomFromCoreSyntax']


CORE_JAVASCRIPT_PACKAGE = ResourcePath('Packages/JavaScript')
CORE_SYNTAX_PATH = CORE_JAVASCRIPT_PACKAGE / 'JavaScript.sublime-syntax'
CORE_TESTS_PATH = CORE_JAVASCRIPT_PACKAGE / 'tests'

BASE_SYNTAX_PATH = PACKAGE_PATH / 'src/syntax/JavaScript.yaml'
TEST_SUITES_PATH = PACKAGE_PATH / 'tests/syntax_test_suites'


# For internal use only.
class UpdateJsCustomFromCoreSyntax(sublime_plugin.ApplicationCommand):
    def run(self):
        CORE_SYNTAX_PATH.copy(BASE_SYNTAX_PATH.file_path())

        for test_path in CORE_TESTS_PATH.children():
            if 'jsx' in test_path.name:
                test_path.copy((TEST_SUITES_PATH / 'jsx' / test_path.name).file_path())
            elif 'typescript' in test_path.name:
                test_path.copy((TEST_SUITES_PATH / 'typescript' / test_path.name).file_path())
            else:
                test_path.copy((TEST_SUITES_PATH / 'base' / test_path.name).file_path())
