import sublime_plugin

from ..settings import get_settings


__all__ = ['SetSyntaxListener']


class SetSyntaxListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        if (
            get_settings()['auto_set_syntax']
            and view.match_selector(0, 'source.js')
        ):
            view.run_command('auto_set_js_custom_syntax')
