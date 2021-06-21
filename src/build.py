import re
from yamlmacros import build

from .paths import PACKAGE_PATH
from .util import merge
from .atomic import atomic_replace

if False:  # Mypy
    from typing import Any


__all__ = ['build_configuration']


SOURCE_PATH = PACKAGE_PATH / 'src/syntax/JS Custom.sublime-syntax.yaml-macros'


def build_configuration(
    name: str,
    configuration: dict,
    destination_path: str,
    output: 'Any'
) -> None:
    source_text = SOURCE_PATH.read_text()

    with atomic_replace(destination_path) as temp:
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
