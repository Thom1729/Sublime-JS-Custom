import sublime
import sublime_plugin

import webbrowser
import urllib.parse

__all__ = ['JsCustomReportSyntaxIssue']


class JsCustomReportSyntaxIssue(sublime_plugin.TextCommand):
    def run(self, edit) -> None:
        parameters = {
            'template': '01-syntax-highlighting.yml',
            'sublime-version': sublime.version(),
            'configuration-name': self.view.syntax().name,
            'code': self.view.substr(sublime.Region(0, self.view.size())),
        }

        try:
            parameters['settings'] = sublime.load_resource('Packages/User/JS Custom.sublime-settings')
        except OSError:
            pass

        url = urllib.parse.urlunparse((
            'https', 'github.com', '/Thom1729/Sublime-JS-Custom/issues/new',
            '', urllib.parse.urlencode(parameters), '',
        ))
        webbrowser.open(url)
