import sublime
import sublime_plugin

import os
from os import path

from YAMLMacros.src.build import build_yaml_macros

ROOT = path.dirname(__file__)
SOURCE_PATH = path.join(ROOT, 'JS Custom.sublime-syntax.yaml-macros')
# SYNTAXES_PATH = target = path.join(ROOT, 'syntaxes')
SYNTAXES_PATH = target = path.join(sublime.packages_path(), 'User', 'JS Custom')

if not os.path.exists(SYNTAXES_PATH):
    os.makedirs(SYNTAXES_PATH)
    sublime.run_command('build_js_custom_syntaxes')

SETTINGS = sublime.load_settings('JS Custom.sublime-settings')

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

old_configurations = get_configurations()
def rebuild_syntaxes():
    global old_configurations

    new_configurations = get_configurations()
    
    changed = [
        name
        for name, configuration in new_configurations.items()
        if old_configurations.get(name, None) != configuration
    ]

    if changed:
        sublime.run_command('build_js_custom_syntaxes', { 'versions': changed })

    old_configurations = new_configurations

SETTINGS.clear_on_change('JSCustom')
SETTINGS.add_on_change('JSCustom', rebuild_syntaxes)

class BuildJsCustomSyntaxesCommand(sublime_plugin.ApplicationCommand):
    def run(self, versions=None):
        os.chdir(ROOT)

        configurations = get_configurations()
        if not versions:
            versions = [ name for name, _ in configurations.items() ]

        with open(SOURCE_PATH, 'r') as file:
            text = file.read()

        def build(version):
            name = 'JS Custom (%s)' % version

            options = configurations[version]
            options['name'] = options.get('name', name)            

            print('Building %s.' % name)
            result = build_yaml_macros(text, context=options)

            target_path = path.join(SYNTAXES_PATH, name + '.sublime-syntax')
            with open(target_path, 'w') as output_file:
                result(output_file)

        for name in versions:
            build(name)
