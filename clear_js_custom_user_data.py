import sublime_plugin
import shutil

from .src.paths import USER_DATA_PATH


class ClearJsCustomUserDataCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        shutil.rmtree(str(USER_DATA_PATH.file_path()), ignore_errors=True)
