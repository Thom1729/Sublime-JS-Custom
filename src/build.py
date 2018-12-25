import re
from threading import Thread
from yamlmacros import build

from .paths import PACKAGE_PATH
from .util import merge
from .atomic import atomic_replace


__all__ = ['build_configurations']


SOURCE_PATH = PACKAGE_PATH / 'src/syntax/JS Custom.sublime-syntax.yaml-macros'


def build_configurations(configurations, destination_path, output=None):
    def run():
        source_text = SOURCE_PATH.read_text()

        for name, configuration in configurations.items():
            with atomic_replace(
                (destination_path / (name + '.sublime-syntax')).file_path()
            ) as temp:
                build(
                    source_text=source_text,
                    destination_path=temp.name,
                    arguments=merge({
                        'name': 'JS Custom - {}'.format(name),
                        'scope': 'source.js.{}'.format(re.sub(r'[^\w-]', '', name.lower())),
                        'file_path': str(SOURCE_PATH.file_path()),
                    }, configuration),
                    error_stream=output,
                )
    Thread(target=run).start()
