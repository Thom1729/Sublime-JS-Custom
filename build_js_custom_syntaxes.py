import sublime
import sublime_plugin

import os
from os import path

from package_control import events
from sublime_lib.output_panel import OutputPanel

from .src.paths import clean_syntaxes, clear_user_data, compiled_syntaxes_system_path
from .src.build import build_configurations
from .src.configurations import ConfigurationManager

def plugin_loaded():
    global configuration_manager
    configuration_manager = ConfigurationManager('JS Custom')
    configuration_manager.add_on_change(auto_build)

    ensure_sanity()

    if events.install('JS Custom'):
        print('JS Custom: New installation. Building all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')
    elif events.post_upgrade('JS Custom'):
        print('JS Custom: Installation upgraded. Rebuilding all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')

def plugin_unloaded():
    if events.remove('JS Custom'):
        print('JS Custom: Uninstalling. Removing all syntaxes.')
        clear_user_data()

def ensure_sanity():
    from package_control import sys_path

    try:
        import ruamel.yaml
    except ImportError:
        sys_path.add_dependency('ruamel-yaml')

    try:
        import yamlmacros
    except ImportError:
        sys_path.add_dependency('yaml_macros_engine')

def auto_build(new_configurations, old_configurations):
    if not configuration_manager.get_setting('auto_build', False): return

    changed = [
        name
        for name in ( set(old_configurations) | set(new_configurations) )
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        print('JS Custom: Configuration changed. Rebuilding some syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes', { 'versions': changed })

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        
        configurations = configuration_manager.get_configurations()

        output_path = compiled_syntaxes_system_path()

        clean_syntaxes(keep=set(configurations))

        if versions:
            configurations = {
                name: configurations[name]
                for name in versions
            }

        build_configurations(configurations, output_path, output)
