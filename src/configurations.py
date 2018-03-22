import sublime

from .util import merge

class ConfigurationManager():
    def __init__(self, name):
        self.listeners = []
        self.settings = sublime.load_settings(name + '.sublime-settings')
        self.old_configurations = self.get_configurations()

        self.settings.clear_on_change(name)
        self.settings.add_on_change(name, self._handle_settings_change)

    def get_setting(self, key, defaultValue=None):
        return self.settings.get(key, defaultValue)

    def get_configurations(self):
        defaults = self.settings.get('defaults')
        return {
            name: merge(defaults, config)
            for name, config in self.settings.get('configurations').items()
        }

    def _handle_settings_change(self):
        new_configurations = self.get_configurations()

        for callback in self.listeners:
            callback(new_configurations, self.old_configurations)

        self.old_configurations = new_configurations

    def add_on_change(self, callback):
        self.listeners.append(callback)
