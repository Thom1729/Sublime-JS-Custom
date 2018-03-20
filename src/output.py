import sublime

from .util import coalesce

class ViewOutputStream():
    def __init__(self, view, scroll_to_end=False):
        self.view = view
        self.scroll_to_end = scroll_to_end

    def write(self, text, scroll_to_end=None):
        self.view.run_command('append', {
            'characters': text,
            'scroll_to_end': coalesce(scroll_to_end, self.scroll_to_end)
        })

    def print(self, text='', scroll_to_end=None):
        self.write(text + '\n', scroll_to_end)

    def clear(self):
        self.view.run_command('clear_view')

class OutputPanel(ViewOutputStream):
    def __init__(self, window, name, *, show=True, settings=None, **kwargs):
        super().__init__(window.create_output_panel(name), **kwargs)

        self.window = window
        self.name = name

        if settings:
            s = self.view.settings()
            for key, value in settings.items():
                s.set(key, value)

        if show: self.show()

    def show(self):
        self.window.run_command('show_panel', {'panel': 'output.%s' % self.name})
