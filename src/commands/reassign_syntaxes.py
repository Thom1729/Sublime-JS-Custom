import sublime
import sublime_plugin

if False:  # Mypy
    from collections.abc import Container

__all__ = ['ReassignSyntaxesCommand']


class ReassignSyntaxesCommand(sublime_plugin.ApplicationCommand):
    def run(self, syntaxes: 'Container[str]', replacement: str) -> None:  # type: ignore
        for window in sublime.windows():
            for view in window.views():
                syntax = view.settings().get('syntax')
                if syntax in syntaxes:
                    view.assign_syntax(replacement)
