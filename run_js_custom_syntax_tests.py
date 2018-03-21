import sublime
import sublime_plugin

import os
from os import path
from itertools import groupby

from .src.output import OutputPanel
from .src.paths import resource_path, system_path, TEST_PATH
from .src.build import build_configurations

def run_syntax_tests(tests, output):
    import sublime_api

    total_assertions = 0
    failed_assertions = 0

    for t in tests:
        assertions, test_output_lines = sublime_api.run_syntax_test(t)
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
    output.print('[Finished]')

class RunJsCustomSyntaxTestsCommand(sublime_plugin.WindowCommand):
    def run(self):
        output = OutputPanel(self.window, 'YAMLMacros', scroll_to_end=True)

        cases = sublime.decode_value(sublime.load_resource('Packages/JSCustom/tests/tests.json'));

        import shutil
        shutil.rmtree(system_path(TEST_PATH))
        os.makedirs(system_path(TEST_PATH))

        syntax_tests = [
            {
                'filename': path.basename(file_path),
                'contents': sublime.load_resource(file_path),
                'suite': path.basename(path.dirname(file_path)),
            }
            for file_path in sublime.find_resources('syntax_test*')
            if file_path.startswith('Packages/JSCustom/tests')
        ]

        syntax_tests.sort(key=lambda test: ( test['suite'], test['filename'] ))

        suites = {
            k: list(v)
            for k,v in groupby(syntax_tests, key=lambda test:test['suite'])
        }

        for name, case in cases.items():
            p = system_path(TEST_PATH, name)
            
            os.makedirs(p)

            build_configurations({ name: case['configuration'] }, p, output)

            syntax_path = resource_path(TEST_PATH, name, name+'.sublime-syntax')

            tests = []

            for suite_name in case['tests']:
                for test in suites[suite_name]:
                    with open(system_path(TEST_PATH, name, test['filename']), 'w') as file:
                        file.write('// SYNTAX TEST "%s"\n' % syntax_path)
                        file.write(test['contents'])

                    tests.append(resource_path(TEST_PATH, name, test['filename']))
            
            run_syntax_tests(tests, output)
