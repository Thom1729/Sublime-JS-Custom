import sublime
import sublime_plugin

__all__ = ['ReassignSyntaxesCommand']


class ReassignSyntaxesCommand(sublime_plugin.ApplicationCommand):
    def run(self, syntaxes, replacement):
        for window in sublime.windows():
            for view in window.views():
                syntax = view.settings().get('syntax')
                if syntax in syntaxes:
                    view.assign_syntax(replacement)
