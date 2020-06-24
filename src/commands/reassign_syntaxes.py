import sublime
import sublime_plugin

__all__ = ['ReassignSyntaxesCommand']


class ReassignSyntaxesCommand(sublime_plugin.ApplicationCommand):
    def run(self, syntaxes, replacement):
        for window in sublime.windows():
            for view in window.views():
                settings = view.settings()
                if settings.get('syntax') in syntaxes:
                    print('replacing {} with {}'.format(
                        settings.get('syntax'),
                        replacement
                    ))
                    settings.set('syntax', replacement)
