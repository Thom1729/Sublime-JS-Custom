import sublime_plugin

from sublime_lib import get_syntax_for_scope


__all__ = ['AutoSetJsCustomSyntaxCommand']


class AutoSetJsCustomSyntaxCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        project_data = self.view.window().project_data()

        try:
            syntax = project_data['JSCustom.js_syntax']
        except KeyError:
            return

        if syntax.startswith('scope:'):
            syntax = get_syntax_for_scope(syntax[6:])

        self.view.assign_syntax(syntax)
