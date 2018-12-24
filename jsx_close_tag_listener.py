import sublime_plugin

from .src.settings import get_settings


__all__ = ['JsxCloseTagListener']


class JsxCloseTagListener(sublime_plugin.ViewEventListener):
    def on_text_command(self, command_name, args):
        if (
            command_name == 'close_tag'
            and get_settings()['jsx_close_tag']
            and self.view.match_selector(0, 'source.js')
        ):
            return ('jsx_close_tag', args)
