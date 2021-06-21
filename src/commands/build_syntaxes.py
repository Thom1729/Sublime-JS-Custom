import sublime
import sublime_plugin

from threading import Thread
import logging
from sublime_lib import OutputPanel, get_syntax_for_scope

from ..settings import get_settings
from ..paths import USER_DATA_PATH
from ..build import build_configuration
from ..configurations import get_configurations

if False:  # Mypy
    from typing import Optional, List


__all__ = ['BuildJsCustomSyntaxesCommand', 'BuildJsCustomSyntaxCommand']


logger = logging.getLogger(__name__)


SYNTAXES_BUILD_PATH = USER_DATA_PATH / 'Syntaxes'


class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions: 'Optional[List[str]]' = None) -> None:
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        settings = get_settings()
        configurations = get_configurations(settings)

        to_delete = {
            syntax_path.stem: syntax_path
            for syntax_path in SYNTAXES_BUILD_PATH.glob('*.sublime-syntax')
            if syntax_path.stem not in configurations
        }
        to_build = configurations

        if versions is not None:
            not_none_versions = versions

            def filter_by_versions(d: dict) -> dict:
                return {
                    k: v
                    for k, v in d.items()
                    if k in not_none_versions
                }
            to_delete = filter_by_versions(to_delete)
            to_build = filter_by_versions(to_build)

        try:
            SYNTAXES_BUILD_PATH.file_path().mkdir(parents=True)
        except FileExistsError:
            pass

        if settings.get('reassign_when_deleting', False):
            replacement = settings['reassign_when_deleting']
            assert isinstance(replacement, str)
            if replacement.startswith('scope:'):
                replacement = get_syntax_for_scope(replacement[6:])

            paths_to_delete = [str(path) for path in to_delete.values()]

            sublime.run_command('reassign_syntaxes', {
                'syntaxes': paths_to_delete,
                'replacement': replacement,
            })

        def run() -> None:
            for name, syntax_path in to_delete.items():
                logger.info('Deleting configuration {}…'.format(name))
                syntax_path.file_path().unlink()

            for name, configuration in to_build.items():
                logger.info('Building configuration {}…'.format(name))
                destination_path = (SYNTAXES_BUILD_PATH / (name + '.sublime-syntax')).file_path()
                build_configuration(name, configuration, str(destination_path), output)

        Thread(target=run).start()


class BuildJsCustomSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, name: str, configuration: dict, destination_path: str) -> None:
        logger.info('Directly building to {}…'.format(destination_path))

        output = OutputPanel.create(self.window, 'YAMLMacros')
        # output.show()

        build_configuration(name, configuration, destination_path, output)
