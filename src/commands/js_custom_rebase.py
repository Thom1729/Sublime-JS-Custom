import sublime_plugin
from sublime_lib import ResourcePath

import re

from JSCustom.src.paths import PACKAGE_PATH


CORE_JAVASCRIPT_PATH = ResourcePath('Packages/JavaScript')

SYNTAX_TEST_FILE_EXPR = re.compile(r"^syntax_test_([a-z]+)")


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
            match = SYNTAX_TEST_FILE_EXPR.match(test.stem)
            if match is None:
                print("Warning: could not determine suite for test {}.".format(test))
                continue
            suite = match.group(1)

            copy(test, PACKAGE_PATH / 'tests/syntax_test_suites' / suite / test.name)
