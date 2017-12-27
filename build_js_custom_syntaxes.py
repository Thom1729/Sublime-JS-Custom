import sublime
import sublime_plugin

import os
from os import path
import time

from package_control import events

def plugin_loaded():
    global ROOT
    ROOT = path.abspath(path.dirname(__file__))

    global SOURCE_PATH
    SOURCE_PATH = path.join(ROOT, 'src', 'JS Custom.sublime-syntax.yaml-macros')

    global USER_PATH
    USER_PATH = path.join(sublime.packages_path(), 'User', 'JS Custom')

    global SYNTAXES_PATH
    SYNTAXES_PATH = path.join(USER_PATH, 'Syntaxes')

    global SETTINGS
    SETTINGS = sublime.load_settings('JS Custom.sublime-settings')

    global old_configurations
    old_configurations = get_configurations()

    SETTINGS.clear_on_change('JSCustom')
    SETTINGS.add_on_change('JSCustom', rebuild_syntaxes)

def is_yaml_macros_installed():
    try:
        from YAMLMacros.api import process_macros
        return True
    except ImportError:
        return False

def ensure_sanity():
    if not is_yaml_macros_installed():
        ret = sublime.yes_no_cancel_dialog(
            'JS Custom requires the YAML Macros package. Install YAML Macros via Package Control?',
            'Install YAML Macros'
        )

        if ret:
            sublime.active_window().run_command(
                'advanced_install_package',
                { 'packages': 'YAMLMacros' },
            )

    if not path.exists(SYNTAXES_PATH):
        os.makedirs(SYNTAXES_PATH)
        sublime.run_command('build_js_custom_syntaxes')

def merge(*dicts):
    ret = {}
    for d in dicts:
        ret.update(d)
    return ret

def get_configurations():
    defaults = SETTINGS.get('defaults')
    return {
        name: merge(defaults, config)
        for name, config in SETTINGS.get('configurations').items()
    }

def rebuild_syntaxes():
    global old_configurations
    new_configurations = get_configurations()
    
    changed = [
        name
        for name, configuration in new_configurations.items()
        if old_configurations.get(name, None) != configuration
    ]

    if changed:
        sublime.active_window().run_command('build_js_custom_syntaxes', { 'versions': changed })

    old_configurations = new_configurations

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        os.chdir(ROOT)

        ensure_sanity()

        with open(SOURCE_PATH, 'r') as source_file:
            source_text = source_file.read()

        configurations = get_configurations().items()
        if versions:
            configurations = [
                (name, configuration)
                for name, configuration in configurations
                if name in versions
            ]

        from YAMLMacros.api import build
        from YAMLMacros.src.output_panel import OutputPanel
        from YAMLMacros.src.error_highlighter import ErrorHighlighter

        panel = OutputPanel(self.window, 'YAMLMacros')
        error_highlighter = ErrorHighlighter(self.window, 'YAMLMacros')

        for name, configuration in configurations:
            name = 'JS Custom (%s)' % name

            build(
                source_text=source_text,
                destination_path=path.join(SYNTAXES_PATH, name + '.sublime-syntax'),
                arguments=merge({
                    'name': name,
                    'file_path': SOURCE_PATH,
                }, configuration),
                error_stream=panel,
                error_highlighter=error_highlighter
            )
