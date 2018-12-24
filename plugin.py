import sublime

from package_control import events
from package_control.package_manager import PackageManager
from package_control.sys_path import add_dependency

from .src.settings import get_settings
from .src.configurations import get_configurations

from .src.commands.build_syntaxes import BuildJsCustomSyntaxesCommand
from .src.commands.clear_user_data import ClearJsCustomUserDataCommand
from .src.commands.jsx_close_tag import JsxCloseTagCommand
from .src.listeners.jsx_close_tag import JsxCloseTagListener


__all__ = [
    'plugin_loaded', 'plugin_unloaded',
    'BuildJsCustomSyntaxesCommand', 'ClearJsCustomUserDataCommand', 'JsxCloseTagCommand',
    'JsxCloseTagListener',
]


PACKAGE_NAME = 'JSCustom'


def plugin_loaded():
    global UNSUBSCRIBE
    UNSUBSCRIBE = get_settings().subscribe(get_configurations, auto_build)

    if events.install(PACKAGE_NAME):
        ensure_dependencies_loaded()
        print('JS Custom: New installation. Building all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')

    elif events.post_upgrade(PACKAGE_NAME):
        ensure_dependencies_loaded()
        print('JS Custom: Installation upgraded. Rebuilding all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')


def plugin_unloaded():
    if UNSUBSCRIBE:
        UNSUBSCRIBE()

    if events.remove(PACKAGE_NAME):
        print('JS Custom: Uninstalling. Removing all syntaxes.')
        sublime.run_command('clear_js_custom_user_data')


def ensure_dependencies_loaded():
    for dependency in PackageManager().get_dependencies('JSCustom'):
        add_dependency(dependency)


def auto_build(new_configurations, old_configurations):
    if not get_settings().get('auto_build', False):
        return

    changed = [
        name
        for name in set(old_configurations) | set(new_configurations)
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        print('JS Custom: Configuration changed. Rebuilding some syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes', {'versions': changed})
