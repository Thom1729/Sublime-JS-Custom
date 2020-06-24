import sublime
import sublime_plugin

from threading import Thread
from sublime_lib import OutputPanel, get_syntax_for_scope

from ..settings import get_settings
from ..paths import USER_DATA_PATH
from ..build import build_configuration
from ..configurations import get_configurations

__all__ = ['BuildJsCustomSyntaxesCommand', 'BuildJsCustomSyntaxCommand']


SYNTAXES_BUILD_PATH = USER_DATA_PATH / 'Syntaxes'


class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        settings = get_settings()
        configurations = get_configurations(settings)

        to_delete = {
            syntax_path.stem : syntax_path
            for syntax_path in SYNTAXES_BUILD_PATH.glob('*.sublime-syntax')
            if syntax_path.stem not in configurations
        }
        to_build = configurations

        if versions is not None:
            def filter_by_versions(d):
                return {
                    k:v
                    for k,v in d.items()
                    if k in versions
                }
            to_delete = filter_by_versions(to_delete)
            to_build = filter_by_versions(to_build)

        try:
            SYNTAXES_BUILD_PATH.file_path().mkdir(parents=True)
        except FileExistsError:
            pass

        if settings.get('reassign_when_deleting', False):
            replacement = settings['reassign_when_deleting']
            if replacement.startswith('scope:'):
                replacement = get_syntax_for_scope(replacement[6:])

            paths_to_delete = [str(path) for path in to_delete.values()]

            print(paths_to_delete, replacement)
            sublime.run_command('reassign_syntaxes', {
                'syntaxes': paths_to_delete,
                'replacement': replacement,
            })

        def run():
            for name, syntax_path in to_delete.items():
                print('JS Custom: Deleting configuration {}…'.format(name))
                syntax_path.file_path().unlink()

            for name, configuration in to_build.items():
                print('JS Custom: Building configuration {}…'.format(name))
                destination_path = (SYNTAXES_BUILD_PATH / (name + '.sublime-syntax')).file_path()
                build_configuration(name, configuration, destination_path, output)

        Thread(target=run).start()


class BuildJsCustomSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, name, configuration, destination_path):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        build_configuration(name, configuration, destination_path, output)
