import sublime_plugin
from sublime_lib import ResourcePath

from ..paths import PACKAGE_PATH

import logging


CORE_JAVASCRIPT_PATH = ResourcePath('Packages/JavaScript')
SYNTAX_TEST_PREFIX = 'syntax_test_'

__all__ = ['JsCustomRebaseCommand']


logger = logging.getLogger(__name__)


def copy(source: ResourcePath, dest: ResourcePath) -> None:
    source_path = source
    dest_path = dest.file_path()

    logger.info("Copying {} to {}…".format(source_path, dest_path))
    source_path.copy(dest_path)


class JsCustomRebaseCommand(sublime_plugin.ApplicationCommand):
    def run(self) -> None:
        copy(
            CORE_JAVASCRIPT_PATH / 'JavaScript.sublime-syntax',
            PACKAGE_PATH / 'src/syntax/JavaScript.yaml'
        )
        copy(
            CORE_JAVASCRIPT_PATH / 'TypeScript.sublime-syntax',
            PACKAGE_PATH / 'extensions/typescript.syntax-extension'
        )
        copy(
            CORE_JAVASCRIPT_PATH / 'JSX.sublime-syntax',
            PACKAGE_PATH / 'extensions/jsx.syntax-extension'
        )
        copy(
            CORE_JAVASCRIPT_PATH / 'TSX.sublime-syntax',
            PACKAGE_PATH / 'extensions/tsx.syntax-extension'
        )

        for test in (CORE_JAVASCRIPT_PATH / 'tests').children():
            if test.stem.startswith(SYNTAX_TEST_PREFIX):
                suite = test.stem[len(SYNTAX_TEST_PREFIX):].split('_')[0]
                destination_name = test.name[len(SYNTAX_TEST_PREFIX):]
            else:
                logger.warn("Could not determine suite for test {}.".format(test))

            copy(test, PACKAGE_PATH / 'tests/syntax_test_suites' / suite / destination_name)
