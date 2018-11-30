import sublime
import sublime_plugin

import os
from os import path
import re

from package_control import events
from sublime_lib.output_panel import OutputPanel
from sublime_lib.settings_dict import NamedSettingsDict

SOURCE_PATH = 'Packages/JSCustom/src/JS Custom.sublime-syntax.yaml-macros'

def plugin_loaded():
    global SYNTAXES_PATH
    SYNTAXES_PATH = path.join(sublime.packages_path(), 'User', 'JS Custom', 'Syntaxes')

    global SETTINGS
    SETTINGS = NamedSettingsDict('JS Custom.sublime-settings')

    if events.install("JSCustom") or events.post_upgrade("JSCustom"):
        def build():
            sublime.active_window().run_command('build_js_custom_syntaxes')

        sublime.set_timeout_async(build, 500)

    global UNSUBSCRIBE
    UNSUBSCRIBE = SETTINGS.subscribe(get_configurations, auto_build)

def plugin_unloaded():
    if UNSUBSCRIBE:
       UNSUBSCRIBE()

def merge(*dicts):
    ret = {}
    for d in dicts:
        ret.update(d)
    return ret

def get_configurations(settings):
    configs = settings['configurations']
    if settings['embed_configuration']:
        configs = merge(
            { '~embed': settings['embed_configuration'] },
            settings['configurations']
        )

    return {
        name: merge(settings['defaults'], config)
        for name, config in configs.items()
    }

def auto_build(new_configurations, old_configurations):
    if not SETTINGS['auto_build']: return

    changed = [
        name
        for name in ( set(old_configurations) | set(new_configurations) )
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        sublime.active_window().run_command('build_js_custom_syntaxes', { 'versions': changed })

class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        from yamlmacros import build

        panel = OutputPanel.create(self.window, 'YAMLMacros')
        panel.show()

        os.makedirs(SYNTAXES_PATH, exist_ok=True)

        source_text = sublime.load_resource('Packages/JSCustom/src/JS Custom.sublime-syntax.yaml-macros')

        configurations = get_configurations(SETTINGS)
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
                    'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
                    'file_path': SOURCE_PATH,
                }, configurations[name]),
                error_stream=panel,
            )
