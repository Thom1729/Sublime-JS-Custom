import sublime
import sublime_plugin

from os import path

from sublime_lib import OutputPanel

from .src.build import build_configuration
from .src.paths import clean_tests, USER_DATA_PATH


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

    for test in tests:
        x = p / test['filename']
        with x.file_path().open('w', encoding='utf-8') as file:
            file.write('// SYNTAX TEST "%s"\n' % str(syntax_path))
            file.write(test['contents'])

    test_paths = [
        p / test['filename']
        for test in tests
    ]

    run_syntax_tests(test_paths, output)


class RunJsCustomSyntaxTestsCommand(sublime_plugin.WindowCommand):
    def run(self):
        clean_tests()

        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        cases = sublime.decode_value(sublime.load_resource('Packages/JSCustom/tests/tests.json'))

        syntax_tests = [
            {
                'filename': path.basename(file_path),
                'contents': sublime.load_resource(file_path),
                'suite': path.basename(path.dirname(file_path)),
            }
            for file_path in sublime.find_resources('syntax_test*')
            if file_path.startswith('Packages/JSCustom/tests')
        ]

        for name, case in cases.items():
            tests = [
                test
                for test in syntax_tests
                if test['suite'] in case['tests']
            ]

            run_tests_for_configuration(name, case['configuration'], output, tests)
