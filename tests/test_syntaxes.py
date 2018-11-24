import sublime_api

from unittesting import DeferrableTestCase

from JSCustom.src.build import build_configurations
from JSCustom.src.paths import clean_tests, PACKAGE_PATH, USER_DATA_PATH


class TestSyntaxes(DeferrableTestCase):
    maxdiff = None

    @classmethod
    def setUpClass(cls):
        clean_tests()

        cls.all_tests = PACKAGE_PATH.glob('tests/**/syntax_test*')

    def _test_syntaxes(self, name, configuration, tests):
        test_working_path = USER_DATA_PATH / 'Tests' / name
        test_working_path.file_path().mkdir(parents=True)

        test_source_paths = [
            (test_working_path / test_path.name, test_path.read_text())
            for test_path in self.all_tests
            if test_path.parent.name in tests
        ]

        build_configurations({name: configuration}, test_working_path)

        syntax_path = test_working_path / (name + '.sublime-syntax')

        for path, text in test_source_paths:
            with path.file_path().open('w', encoding='utf-8') as file:
                file.write('// SYNTAX TEST "{!s}"\n{}'.format(
                    syntax_path,
                    text
                ))

        yield syntax_path.exists

        all_failures = []
        for path, text in test_source_paths:
            yield path.exists
            assertion_count, failures = sublime_api.run_syntax_test(str(path))
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
