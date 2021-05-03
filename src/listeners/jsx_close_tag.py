import sublime_plugin

from ..settings import get_settings


if False:  # Mypy
    from typing import Optional, Tuple


__all__ = ['JsxCloseTagListener']


class JsxCloseTagListener(sublime_plugin.ViewEventListener):
    def on_text_command(self, command_name: str, args: dict) -> 'Optional[Tuple[str, dict]]':
        if command_name != 'close_tag':
            return None

        selector = get_settings()['jsx_close_tag']

        if not selector:
            return None
        elif selector is True:
            selector = 'source.js, source.ts, source.tsx'

        assert isinstance(selector, str)

        if self.view.match_selector(0, selector):
            return ('jsx_close_tag', args)
        else:
            return None
