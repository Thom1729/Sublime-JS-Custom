import sublime_plugin

from ..settings import get_settings


if False:  # Mypy
    from typing import Optional, Tuple


__all__ = ['JsxCloseTagListener']


class JsxCloseTagListener(sublime_plugin.ViewEventListener):
    def _get_selector(self) -> str:
        selector = get_settings()['jsx_close_tag']

        if not selector:
            return None
        elif selector is True:
            selector = 'source.js, source.ts, source.tsx'

        assert isinstance(selector, str)
        return selector

    def on_text_command(self, command_name: str, args: dict) -> 'Optional[Tuple[str, dict]]':
        if command_name != 'close_tag':
            return None

        selector = self._get_selector()

        if self.view.match_selector(0, selector):
            return ('jsx_close_tag', args)
        else:
            return None

    def on_query_context(self, key: str, operator: int, operand: str, match_all: bool) -> 'Optional[bool]':
        if key == 'in_jsx_close_tag_scope':
            selector = self._get_selector()

            return all(
                self.view.match_selector(r.b, selector)
                for r in self.view.sel()
            )
