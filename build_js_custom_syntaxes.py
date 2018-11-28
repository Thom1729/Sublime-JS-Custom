import sublime
import sublime_plugin

from package_control import events
from sublime_lib import OutputPanel, NamedSettingsDict

from .src.paths import USER_DATA_PATH
from .src.build import build_configurations
from .src.configurations import get_configurations


__all__ = ['plugin_loaded', 'plugin_unloaded', 'BuildJsCustomSyntaxesCommand']


SYNTAXES_BUILD_PATH = USER_DATA_PATH / 'Syntaxes'


def plugin_loaded():
    global SETTINGS
    global UNSUBSCRIBE
    SETTINGS = NamedSettingsDict('JS Custom')
    UNSUBSCRIBE = SETTINGS.subscribe(get_configurations, auto_build)

    ensure_sanity()

    if events.install('JS Custom'):
        print('JS Custom: New installation. Building all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')
    elif events.post_upgrade('JS Custom'):
        print('JS Custom: Installation upgraded. Rebuilding all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')


def plugin_unloaded():
    if UNSUBSCRIBE:
        UNSUBSCRIBE()

    if events.remove('JS Custom'):
        print('JS Custom: Uninstalling. Removing all syntaxes.')
        sublime.run_command('clear_js_custom_user_data')


def ensure_sanity():
    from package_control import sys_path

    try:
        import ruamel.yaml  # noqa: F401
    except ImportError:
        sys_path.add_dependency('ruamel-yaml')

    try:
        import yamlmacros  # noqa: F401
    except ImportError:
        sys_path.add_dependency('yaml_macros_engine')


def auto_build(new_configurations, old_configurations):
    if not SETTINGS.get('auto_build', False):
        return

    changed = [
        name
        for name in set(old_configurations) | set(new_configurations)
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        print('JS Custom: Configuration changed. Rebuilding some syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes', {'versions': changed})


class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        configurations = get_configurations(SETTINGS)

        for syntax_path in SYNTAXES_BUILD_PATH.glob('*.sublime-syntax'):
            if syntax_path.name not in configurations:
                syntax_path.file_path().unlink()

        try:
            SYNTAXES_BUILD_PATH.file_path().mkdir(parents=True)
        except FileExistsError:
            pass

        if versions:
            configurations = {
                name: configurations[name]
                for name in versions
            }

        build_configurations(configurations, SYNTAXES_BUILD_PATH, output)
