import re
import traceback
from os import path

from yamlmacros import builds

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

    output.write('Building %s…\n' % (name))

    try:
        text = builds(
            source_text=source_text,
            arguments={
                'configuration': merge({
                    'name': 'JS Custom - {}'.format(name),
                    'scope': 'source.js.{}'.format(re.sub(r'[^\w-]', '', name.lower())),
                }, configuration)
            },
        )

        with atomic_replace(destination_path) as temp:
            temp.write(text)
            output.write('Compiled to %s. (%s)\n' % (path.basename(temp.name), temp.name))
    except Exception as e:
        output.write(''.join(traceback.format_exception(None, e, e.__traceback__)))
        output.write('Failed\n\n')
        return

    output.write('Succeeded\n\n')
