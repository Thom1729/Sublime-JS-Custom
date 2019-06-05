import sublime_api
import shutil

from unittesting import DeferrableTestCase

from JSCustom.src.build import build_configurations
from JSCustom.src.paths import PACKAGE_PATH, USER_DATA_PATH


TESTS_PATH = USER_DATA_PATH / 'Tests'
TEST_SUITES_PATH = PACKAGE_PATH / 'tests/syntax_test_suites'

SYNTAX_DELAY = 200


class TestSyntaxes(DeferrableTestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        shutil.rmtree(str(TESTS_PATH.file_path()), ignore_errors=True)
        TESTS_PATH.file_path().mkdir(parents=True)

        cls.all_tests = TEST_SUITES_PATH.rglob('syntax_test*')

    def _test_syntaxes(self, name, configuration, tests):
        test_working_path = TESTS_PATH / name
        test_working_path.file_path().mkdir(parents=True)

        build_configurations({name: configuration}, test_working_path)
        syntax_path = test_working_path / (name + '.sublime-syntax')

        yield syntax_path.exists
        yield SYNTAX_DELAY  # Hope this gives Sublime long enough to compile it.

        syntax_test_header = '// SYNTAX TEST "{!s}"\n'.format(syntax_path)
        all_failures = []

        for test_source in self.all_tests:
            if test_source.parent.name in tests:
                test_dest = test_working_path / test_source.name
                text = test_source.read_text().split('\n', 1)[1]

                with test_dest.file_path().open('w', encoding='utf-8') as file:
                    file.write(syntax_test_header)
                    file.write(text)

                yield test_dest.exists
                assertion_count, failures = sublime_api.run_syntax_test(str(test_dest))

                if failures and failures[0].endswith('does not match scope [text.plain]'):
                    raise RuntimeError('Sublime did no compile {!s} in time.'.format(test_dest))
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
