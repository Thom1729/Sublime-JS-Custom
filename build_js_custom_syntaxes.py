import sublime
import sublime_plugin

import os
from os import path

from package_control import events

from .src.output import OutputPanel
from .src.util import merge
from .src.paths import resource_path, system_path
from .src.build import build_configurations

def plugin_loaded():
    global SYNTAXES_PATH
    SYNTAXES_PATH = system_path('User', 'JS Custom', 'Syntaxes')
    
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

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        output = OutputPanel(self.window, 'YAMLMacros', scroll_to_end=True)
        
        configurations = get_configurations()

        clean_output_directory(SYNTAXES_PATH, keep=set(configurations))

        if versions:
            configurations = {
                name: configurations[name]
                for name in versions
            }

        build_configurations(configurations, SYNTAXES_PATH, output)
