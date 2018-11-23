import re

from .paths import SOURCE_PATH
from .util import merge


__all__ = ['build_configurations', 'build_configuration']


def build_configurations(configurations, destination_path, output):
    from yamlmacros import build

    source_text = SOURCE_PATH.read_text()

    for name, configuration in configurations.items():
        d = str(destination_path / (name + '.sublime-syntax'))
        build(
            source_text=source_text,
            destination_path=d,
            arguments=merge({
                'name': 'JS Custom - %s' % name,
                'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
                'file_path': str(SOURCE_PATH.file_path()),
            }, configuration),
            error_stream=output,
        )


def build_configuration(name, configuration, destination_path, output):
    from yamlmacros import build

    source_text = SOURCE_PATH.read_text()

    d = str((destination_path / (name + '.sublime-syntax')).file_path())
    build(
        source_text=source_text,
        destination_path=d,
        arguments=merge({
            'name': 'JS Custom - %s' % name,
            'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
            'file_path': str(SOURCE_PATH.file_path()),
        }, configuration),
        error_stream=output,
    )
