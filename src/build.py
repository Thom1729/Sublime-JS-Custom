import re

from .paths import PACKAGE_PATH
from .util import merge
from .defer import defer_each
from .atomic import atomic_replace


__all__ = ['build_configurations']


SOURCE_PATH = PACKAGE_PATH / 'src/syntax/JS Custom.sublime-syntax.yaml-macros'


def build_configurations(configurations, destination_path, output=None):
    from yamlmacros import build

    source_text = SOURCE_PATH.read_text()

    def _build(value):
        name, configuration = value

        with atomic_replace(
            (destination_path / (name + '.sublime-syntax')).file_path()
        ) as temp:
            build(
                source_text=source_text,
                destination_path=temp.name,
                arguments=merge({
                    'name': 'JS Custom - %s' % name,
                    'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
                    'file_path': str(SOURCE_PATH.file_path()),
                }, configuration),
                error_stream=output,
            )

    defer_each(_build, configurations.items())
