import sublime
import sublime_plugin

import os
from os import path

from YAMLMacros.src.build import build_yaml_macros

class BuildCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, version='Default'):
        root = path.dirname(__file__)

        os.chdir(path.join(root, 'syntaxes'))


        options = sublime.load_settings('JS Custom.sublime-settings').get(version)

        # input_path = path.join(root, 'syntaxes', 'JS Custom (%s).sublime-syntax.yaml-macros' % version)

        view = self.window.active_view();
        text = view.substr( sublime.Region(0, view.size()) )

        output_path = path.join(root, 'compiled', 'JS Custom (%s).sublime-syntax' % version)

        with open(output_path, 'w') as output_file:

            build_yaml_macros(
                text,
                output_file,
                options,
            )
