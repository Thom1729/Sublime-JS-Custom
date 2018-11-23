import sublime
import sublime_plugin

from sublime_lib import OutputPanel

from .src.build import build_configuration
from .src.paths import clean_tests, USER_DATA_PATH, PACKAGE_PATH


__all__ = ['RunJsCustomSyntaxTestsCommand']


def run_syntax_tests(tests, output):
    import sublime_api

    total_assertions = 0
    failed_assertions = 0

    for t in tests:
        assertions, test_output_lines = sublime_api.run_syntax_test(str(t))
        total_assertions += assertions
        if len(test_output_lines) > 0:
            failed_assertions += len(test_output_lines)
            for line in test_output_lines:
                output.print(line)

    if failed_assertions > 0:
        message = 'FAILED: {} of {} assertions in {} files failed'
        params = (failed_assertions, total_assertions, len(tests))
    else:
        message = 'Success: {} assertions in {} files passed'
        params = (total_assertions, len(tests))

    output.print(message.format(*params))
    output.print()


def run_tests_for_configuration(name, configuration, output, tests):
    p = USER_DATA_PATH / 'Tests' / name

    p.file_path().mkdir(parents=True)

    build_configuration(name, configuration, p, output)

    syntax_path = p / (name + '.sublime-syntax')

    for test_path in tests:
        x = p / test_path.name
        with x.file_path().open('w', encoding='utf-8') as file:
            file.write('// SYNTAX TEST "{}"\n{}'.format(
                str(syntax_path),
                test_path.read_text()
            ))

    test_paths = [
        p / test_path.name
        for test_path in tests
    ]

    run_syntax_tests(test_paths, output)


class RunJsCustomSyntaxTestsCommand(sublime_plugin.WindowCommand):
    def run(self):
        clean_tests()

        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        from sublime_lib import ResourcePath

        cases = sublime.decode_value(
            (PACKAGE_PATH / 'tests/tests.json').read_text()
        )

        syntax_tests = PACKAGE_PATH.glob('tests/**/syntax_test*')

        for name, case in cases.items():
            tests = [
                test_path
                for test_path in syntax_tests
                if test_path.parent.name in case['tests']
            ]

            run_tests_for_configuration(name, case['configuration'], output, tests)
