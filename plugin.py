import sublime

from package_control import events

from .src.logging import initialize_logger
from .src.paths import PACKAGE_PATH
from .src.settings import get_settings
from .src.configurations import get_configurations

from .src.commands.build_syntaxes import BuildJsCustomSyntaxesCommand, BuildJsCustomSyntaxCommand
from .src.commands.build_tests import BuildJsCustomTestsCommand
from .src.commands.clear_user_data import ClearJsCustomUserDataCommand
from .src.commands.reassign_syntaxes import ReassignSyntaxesCommand
from .src.commands.jsx_close_tag import JsxCloseTagCommand
from .src.commands.js_custom_rebase import JsCustomRebaseCommand
from .src.commands.report_syntax_issue import JsCustomReportSyntaxIssue
from .src.listeners.jsx_close_tag import JsxCloseTagListener

import logging


logger = logging.getLogger(__name__)


__all__ = [
    'plugin_loaded', 'plugin_unloaded',
    'BuildJsCustomSyntaxesCommand',
    'BuildJsCustomSyntaxCommand',
    'BuildJsCustomTestsCommand',
    'ClearJsCustomUserDataCommand',
    'ReassignSyntaxesCommand',
    'JsxCloseTagCommand',
    'JsCustomRebaseCommand',
    'JsxCloseTagListener',
]


PACKAGE_NAME = PACKAGE_PATH.package
UNSUBSCRIBE = None


def plugin_loaded() -> None:
    initialize_logger()

    # logger.info("plugin_loaded")

    global UNSUBSCRIBE
    UNSUBSCRIBE = get_settings().subscribe(get_configurations, auto_build)

    if events.install(PACKAGE_NAME):
        logger.info('New installation. Building all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')

    elif events.post_upgrade(PACKAGE_NAME):
        logger.info('Installation upgraded. Building all syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes')


def plugin_unloaded() -> None:
    if UNSUBSCRIBE:
        UNSUBSCRIBE()

    if events.remove(PACKAGE_NAME):
        logger.info('Uninstalling. Removing all syntaxes.')
        sublime.run_command('clear_js_custom_user_data')


def auto_build(new_configurations: dict, old_configurations: dict) -> None:
    if not get_settings().get('auto_build', False):
        return

    changed = [
        name
        for name in set(old_configurations) | set(new_configurations)
        if old_configurations.get(name, None) != new_configurations.get(name, None)
    ]

    if changed:
        logger.info('Configuration changed. Rebuilding some syntaxes.')
        sublime.active_window().run_command('build_js_custom_syntaxes', {'versions': changed})
