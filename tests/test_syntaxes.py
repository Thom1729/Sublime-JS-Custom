import sublime
import sublime_api
import shutil

from unittesting import DeferrableTestCase

from sublime_lib import OutputPanel

from JSCustom.src.build import build_configuration
from JSCustom.src.paths import PACKAGE_PATH, USER_DATA_PATH


TESTS_PATH = USER_DATA_PATH / 'Tests'
TEST_SUITES_PATH = PACKAGE_PATH / 'tests/syntax_test_suites'

SYNTAX_DELAY = 500


class TestSyntaxes(DeferrableTestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        shutil.rmtree(str(TESTS_PATH.file_path()), ignore_errors=True)
        TESTS_PATH.file_path().mkdir(parents=True)

    def _test_syntaxes(self, name, configuration, tests):
        test_working_path = TESTS_PATH / name
        test_working_path.file_path().mkdir(parents=True)

        output = OutputPanel.create(sublime.active_window(), 'YAMLMacros')

        syntax_path = test_working_path / (name + '.sublime-syntax')
        build_configuration(name, configuration, syntax_path.file_path(), output)

        sublime.run_command('build_js_custom_tests', {
            'syntax_path': str(syntax_path),
            'suites': tests,
            'destination_directory': str(test_working_path.file_path()),
        })

        yield syntax_path.exists
        yield SYNTAX_DELAY  # Hope this gives Sublime long enough to compile it.

        all_failures = []

        for test_dest in test_working_path.glob('syntax_test*'):
            assertion_count, failures = sublime_api.run_syntax_test(str(test_dest))

            if failures and failures[0].endswith('does not match scope [text.plain]'):
                raise RuntimeError('Sublime did not compile {!s} in time.'.format(test_dest))
            else:
                all_failures.extend(failures)

        self.assertEqual(all_failures, [])

    def test_base(self):
        yield from self._test_syntaxes(
            name="base",
            configuration={
                "file_extensions": [],
                "hidden": True,
            },
            tests=["base"],
        )

    def test_jsx(self):
        yield from self._test_syntaxes(
            name="jsx",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "jsx": True,
                "es_pipeline": True,
                "es_slice": True,
            },
            tests=["base", "jsx", "pipeline", "slice"],
        )

    def test_flow(self):
        yield from self._test_syntaxes(
            name="flow",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "flow_types": True
            },
            tests=["base", "flow"],
        )

    def test_templates(self):
        yield from self._test_syntaxes(
            name="templates",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "custom_templates": {
                    'tags': {
                        'css': 'scope:source.css',
                    },
                    'comments': {
                        'css': 'scope:source.css',
                    },
                    'lookaheads': {
                        r'select\b': 'scope:source.sql',
                    },
                    'styled_components': True,
                }
            },
            tests=["base", "templates"],
        )

    def test_string_object_keys(self):
        yield from self._test_syntaxes(
            name="string_object_keys",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "string_object_keys": True,
            },
            tests=["base", "string_object_keys"],
        )

    def test_typescript(self):
        yield from self._test_syntaxes(
            name="typescript",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "typescript": True,
            },
            tests=["base", "typescript"],
        )
