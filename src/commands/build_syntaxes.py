import sublime_plugin

from threading import Thread
from sublime_lib import OutputPanel

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

        configurations = get_configurations(get_settings())

        for syntax_path in SYNTAXES_BUILD_PATH.glob('*.sublime-syntax'):
            if syntax_path.stem not in configurations:
                syntax_path.file_path().unlink()

        try:
            SYNTAXES_BUILD_PATH.file_path().mkdir(parents=True)
        except FileExistsError:
            pass

        if versions:
            configurations = {
                name: configurations[name]
                for name in versions
                if name in configurations
            }

        def run():
            for name, configuration in configurations.items():
                destination_path = (SYNTAXES_BUILD_PATH / (name + '.sublime-syntax')).file_path()
                build_configuration(name, configuration, destination_path, output)

        Thread(target=run).start()


class BuildJsCustomSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, name, configuration, destination_path):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        build_configuration(name, configuration, destination_path, output)
