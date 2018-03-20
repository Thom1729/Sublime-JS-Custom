import sublime
import sublime_plugin

import os
from os import path

from package_control import events

from .src.output import OutputPanel
from .src.util import merge

SOURCE_PATH = 'Packages/JSCustom/src/syntax/JS Custom.sublime-syntax.yaml-macros'

def plugin_loaded():
    global SYNTAXES_PATH
    SYNTAXES_PATH = path.join(sublime.packages_path(), 'User', 'JS Custom', 'Syntaxes')
    
    global TEST_SYNTAXES_PATH
    TEST_SYNTAXES_PATH = path.join(sublime.packages_path(), 'User', 'JS Custom', 'Tests')

    global SETTINGS
    SETTINGS = sublime.load_settings('JS Custom.sublime-settings')

    global old_configurations
    old_configurations = get_configurations()

    ensure_sanity()

    SETTINGS.clear_on_change('JSCustom')
    SETTINGS.add_on_change('JSCustom', auto_build)

def is_ruamel_yaml_available():
    try:
        import ruamel.yaml
        return True
    except ImportError:
        return False

def is_yamlmacros_available():
    try:
        import yamlmacros
        return True
    except ImportError:
        return False

def ensure_sanity():
    if not is_ruamel_yaml_available():
        from package_control import sys_path
        sys_path.add_dependency('ruamel-yaml')

    if not is_yamlmacros_available():
        from package_control import sys_path
        sys_path.add_dependency('yaml_macros_engine')

    if not path.exists(SYNTAXES_PATH):
        print("JS Custom: Building syntaxes...")
        os.makedirs(SYNTAXES_PATH)

        def build():
            sublime.active_window().run_command('build_js_custom_syntaxes')

        sublime.set_timeout_async(build, 500)

def get_configurations():
    defaults = SETTINGS.get('defaults')
    return {
        name: merge(defaults, config)
        for name, config in SETTINGS.get('configurations').items()
    }

def auto_build():
    if not SETTINGS.get('auto_build', False): return

    global old_configurations
    new_configurations = get_configurations()

    changed = [
        name
        for name in ( set(old_configurations) | set(new_configurations) )
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        sublime.active_window().run_command('build_js_custom_syntaxes', { 'versions': changed })

    old_configurations = new_configurations

def clean_output_directory(directory_path, keep=set()):
    for filename in os.listdir(directory_path):
        name, ext = path.splitext(filename)
        if ext == '.sublime-syntax' and name not in keep:
            os.remove(path.join(directory_path, filename))
            # TODO: Print something!

def build_configurations(configurations, destination_path, output):
    from yamlmacros import build
    from yamlmacros.src.error_highlighter import ErrorHighlighter

    error_highlighter = ErrorHighlighter(output.window, 'YAMLMacros')

    source_text = sublime.load_resource(SOURCE_PATH)

    for name, configuration in configurations.items():
        build(
            source_text=source_text,
            destination_path=path.join(destination_path, name + '.sublime-syntax'),
            arguments=merge({
                'name': 'JS Custom - %s' % name,
                'file_path': SOURCE_PATH,
            }, configuration),
            error_stream=output,
            error_highlighter=error_highlighter
        )

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        configurations = get_configurations()

        clean_output_directory(SYNTAXES_PATH, keep=set(configurations))

        if versions:
            configurations = {
                name: configurations[name]
                for name in versions
            }

        build_configurations(configurations, SYNTAXES_PATH, output)

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

        configurations = { name: case['configuration'] for name, case in cases.items() }

        if not path.exists(TEST_SYNTAXES_PATH):
            os.makedirs(TEST_SYNTAXES_PATH)

        clean_output_directory(TEST_SYNTAXES_PATH)

        build_configurations(configurations, TEST_SYNTAXES_PATH, output)

        syntax_tests = [
            path
            for path in sublime.find_resources('syntax_test*')
            if path.startswith('Packages/JSCustom/tests')
        ]

        for name, case in cases.items():
            syntax_path = 'Packages/User/JS Custom/Tests/%s.sublime-syntax' % name

            tests = []
            for test_path in syntax_tests:
                filename = path.basename(test_path)
                contents = sublime.load_resource(test_path)

                test_output_path = path.join(TEST_SYNTAXES_PATH, filename)

                with open(test_output_path, 'w') as file:
                    file.write('// SYNTAX TEST "%s"\n' % syntax_path)
                    file.write(contents)

                test_resource_path = path.join('Packages/User/JS Custom/Tests', filename)
                tests.append(test_resource_path)
            
            run_syntax_tests(tests, output)
