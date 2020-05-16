import sublime_plugin

from os.path import join

from JSCustom.src.paths import PACKAGE_PATH


__all__ = ['BuildJsCustomTestsCommand']


TEST_SUITES_PATH = PACKAGE_PATH / 'tests/syntax_test_suites'


class BuildJsCustomTestsCommand(sublime_plugin.ApplicationCommand):
    def run(self, syntax_path, suites, destination_directory):
        syntax_test_header = '// SYNTAX TEST "{!s}"\n'.format(syntax_path)

        test_paths = [
            test_path
            for test_path in TEST_SUITES_PATH.rglob('syntax_test*')
            if test_path.parent.name in suites
        ]

        for source_path in test_paths:
            destination_path = join(destination_directory, source_path.name)
            text = source_path.read_text().split('\n', 1)[1]

            with open(destination_path, 'w', encoding='utf-8') as file:
                file.write(syntax_test_header)
                file.write(text)
