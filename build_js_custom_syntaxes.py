import sublime
import sublime_plugin

import os
from os import path

from package_control import events

SOURCE_PATH = 'Packages/JSCustom/src/JS Custom.sublime-syntax.yaml-macros'

def plugin_loaded():
    global SYNTAXES_PATH
    SYNTAXES_PATH = path.join(sublime.packages_path(), 'User', 'JS Custom', 'Syntaxes')

    global SETTINGS
    SETTINGS = sublime.load_settings('JS Custom.sublime-settings')

    global old_configurations
    old_configurations = get_configurations()

    ensure_sanity()

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
        from package_control.package_manager import PackageManager
        package_manager = PackageManager()
        print("JS Custom: Installing YAML Macros...")
        package_manager.install_package('YAMLMacros', False)

    import sys
    if not any('ruamel-yaml' in p for p in sys.path):
        # Patch dependency path on first run
        sys.path.append(path.join(
            sublime.packages_path(),
            'ruamel-yaml',
            'st3',
        ))

    if not path.exists(SYNTAXES_PATH):
        print("JS Custom: Building syntaxes...")
        os.makedirs(SYNTAXES_PATH)

        def build():
            sublime.active_window().run_command('build_js_custom_syntaxes')

        sublime.set_timeout_async(build, 500)

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
        source_text = sublime.load_resource('Packages/JSCustom/src/JS Custom.sublime-syntax.yaml-macros')

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
