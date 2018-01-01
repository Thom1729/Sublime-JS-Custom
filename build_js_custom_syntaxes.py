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
        import YAMLMacros.api
        return True
    except ImportError:
        return False

def is_ruamel_yaml_available():
    try:
        import ruamel.yaml
        return True
    except ImportError:
        return False

def ensure_sanity():
    if not is_yaml_macros_installed():
        from package_control.package_manager import PackageManager
        package_manager = PackageManager()
        print("JS Custom: Installing YAML Macros...")
        package_manager.install_package('YAMLMacros', False)

    if not is_ruamel_yaml_available():
        from package_control import sys_path
        sys_path.add_dependency('ruamel-yaml')

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
        for name in ( set(old_configurations) | set(new_configurations) )
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        sublime.active_window().run_command('build_js_custom_syntaxes', { 'versions': changed })

    old_configurations = new_configurations

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        from YAMLMacros.api import build
        from YAMLMacros.src.output_panel import OutputPanel
        from YAMLMacros.src.error_highlighter import ErrorHighlighter

        panel = OutputPanel(self.window, 'YAMLMacros')
        error_highlighter = ErrorHighlighter(self.window, 'YAMLMacros')

        print(versions)

        source_text = sublime.load_resource('Packages/JSCustom/src/JS Custom.sublime-syntax.yaml-macros')

        configurations = get_configurations()
        config_names = set(configurations)

        old_syntaxes = [
            file for file in os.listdir(SYNTAXES_PATH)
            if path.splitext(file)[0] not in config_names
            and path.splitext(file)[1] == '.sublime-syntax'
        ]

        for file in old_syntaxes:
            file_path = path.join(SYNTAXES_PATH, file)
            os.remove(file_path)
            panel.print("Removed %s (%s)." % (file, file_path))

        if versions:
            config_names = config_names & set(versions)

        for name in config_names:
            build(
                source_text=source_text,
                destination_path=path.join(SYNTAXES_PATH, name + '.sublime-syntax'),
                arguments=merge({
                    'name': 'JS Custom - %s' % name,
                    'file_path': SOURCE_PATH,
                }, configurations[name]),
                error_stream=panel,
                error_highlighter=error_highlighter
            )
