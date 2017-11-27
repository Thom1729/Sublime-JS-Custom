import sublime
import sublime_plugin

import os
from os import path

from YAMLMacros.src.build import build_yaml_macros

class BuildCustomSyntaxesCommand(sublime_plugin.WindowCommand):
    def run(self, version='Default'):
        root = path.dirname(__file__)

        os.chdir(root)

        options = sublime.load_settings('JS Custom.sublime-settings').get(version)
        options['name'] = 'JS Custom (%s)' % version

        view = self.window.active_view();
        text = view.substr( sublime.Region(0, view.size()) )

        output_path = path.join(root, 'syntaxes', options['name'] + '.sublime-syntax')

        with open(output_path, 'w') as output_file:

            build_yaml_macros(
                text,
                output_file,
                options,
            )
