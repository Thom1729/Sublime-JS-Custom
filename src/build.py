import re

from .paths import SOURCE_PATH
from .util import merge
from .defer import defer_each


__all__ = ['build_configurations']


def build_configurations(configurations, destination_path, output=None):
    from yamlmacros import build

    source_text = SOURCE_PATH.read_text()

    def _build(value):
        name, configuration = value

        d = destination_path / (name + '.sublime-syntax')
        build(
            source_text=source_text,
            destination_path=str(d.file_path()),
            arguments=merge({
                'name': 'JS Custom - %s' % name,
                'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
                'file_path': str(SOURCE_PATH.file_path()),
            }, configuration),
            error_stream=output,
        )

    defer_each(_build, configurations.items())
