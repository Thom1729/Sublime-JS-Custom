import sublime_plugin

from sublime_lib import OutputPanel

from .src.settings import get_settings
from .src.paths import USER_DATA_PATH
from .src.build import build_configurations
from .src.configurations import get_configurations

__all__ = ['BuildJsCustomSyntaxesCommand']


SYNTAXES_BUILD_PATH = USER_DATA_PATH / 'Syntaxes'


class BuildJsCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, versions=None):
        output = OutputPanel.create(self.window, 'YAMLMacros')
        output.show()

        configurations = get_configurations(get_settings())

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
