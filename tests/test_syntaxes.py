import sublime
import sublime_api
import shutil

from unittesting import DeferrableTestCase

from JSCustom.src.paths import PACKAGE_PATH, USER_DATA_PATH


TESTS_PATH = USER_DATA_PATH / 'Tests'
TEST_SUITES_PATH = PACKAGE_PATH / 'tests/syntax_test_suites'


class TestSyntaxes(DeferrableTestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        shutil.rmtree(str(TESTS_PATH.file_path()), ignore_errors=True)
        TESTS_PATH.file_path().mkdir(parents=True)

    def _test_syntaxes(self, *, name, configuration, tests, exclude=[]):
        test_working_path = TESTS_PATH / name
        test_working_path.file_path().mkdir(parents=True)

        syntax_path = test_working_path / (name + '.sublime-syntax')
        sublime.active_window().run_command('build_js_custom_syntax', {
            'name': name,
            'configuration': configuration,
            'destination_path': str(syntax_path.file_path()),
        })

        sublime.run_command('build_js_custom_tests', {
            'syntax_path': str(syntax_path),
            'suites': tests,
            'exclude': exclude,
            'destination_directory': str(test_working_path.file_path()),
        })

        def syntax_exists():
            syntax = sublime.syntax_from_path(str(syntax_path))
            return syntax is not None

        yield syntax_exists

        all_failures = []

        for test_dest in test_working_path.glob('syntax_test*'):
            yield 1
            _, failures = sublime_api.run_syntax_test(str(test_dest))

            if failures and failures[0].endswith('does not match scope [text.plain]'):
                raise RuntimeError('Sublime did not compile {!s} in time.'.format(test_dest))
            else:
                all_failures.extend(failures)

        self.assertEqual(all_failures, [])

    def test_base(self):
        yield from self._test_syntaxes(
            name="js",
            configuration={
                "file_extensions": [],
                "hidden": True,
            },
            tests=["js"],
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
            tests=["js", "jsx", "pipeline", "slice"],
        )

    def test_flow(self):
        yield from self._test_syntaxes(
            name="flow",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "flow_types": True
            },
            tests=["js", "flow"],
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
                    'default': 'scope:text.html.basic',
                }
            },
            tests=["js", "templates"],
            exclude=["js.js"]
        )

    def test_string_object_keys(self):
        yield from self._test_syntaxes(
            name="string_object_keys",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "string_object_keys": True,
            },
            tests=["js", "string_object_keys"],
        )

    def test_typescript_plain(self):
        yield from self._test_syntaxes(
            name="typescript_plain",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "typescript": True,
            },
            tests=["js", "typescript"],
            exclude=["js_not_typescript.js"],
        )

    def test_typescript_jsx(self):
        yield from self._test_syntaxes(
            name="typescript_jsx",
            configuration={
                "file_extensions": [],
                "hidden": True,
                "typescript": True,
                "jsx": True,
            },
            tests=["js", "typescript", "jsx"],
            exclude=["js_not_typescript.js", "typescript_not_tsx.ts"],
        )
