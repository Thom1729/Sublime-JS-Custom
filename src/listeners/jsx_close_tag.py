import sublime_plugin

from ..settings import get_settings


__all__ = ['JsxCloseTagListener']


class JsxCloseTagListener(sublime_plugin.ViewEventListener):
    def on_text_command(self, command_name, args):
        if command_name != 'close_tag':
            return

        selector = get_settings()['jsx_close_tag']

        if not selector:
            return
        elif selector is True:
            selector = 'source.js, source.ts, source.tsx'

        if self.view.match_selector(0, selector):
            return ('jsx_close_tag', args)
