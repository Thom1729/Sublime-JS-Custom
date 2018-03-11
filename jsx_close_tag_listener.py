import sublime
import sublime_plugin

class JsxCloseTagListener(sublime_plugin.ViewEventListener):
    def on_text_command(self, command_name, args):
        if command_name != 'close_tag': return
        if not self.view.match_selector(0, 'source.js'): return

        return ('jsx_close_tag', args)
