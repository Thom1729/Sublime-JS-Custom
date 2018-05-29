import sublime

from os import path
import re

from .paths import SOURCE_PATH
from .util import merge

def build_configurations(configurations, destination_path, output):
    from yamlmacros import build
    from yamlmacros.src.error_highlighter import ErrorHighlighter

    error_highlighter = ErrorHighlighter(output.window, 'YAMLMacros')

    source_text = sublime.load_resource(SOURCE_PATH)

    for name, configuration in configurations.items():
        build(
            source_text=source_text,
            destination_path=path.join(destination_path, name + '.sublime-syntax'),
            arguments=merge({
                'name': 'JS Custom - %s' % name,
                'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
                'file_path': SOURCE_PATH,
            }, configuration),
            error_stream=output,
            error_highlighter=error_highlighter
        )

def build_configuration(name, configuration, destination_path, output):
    from yamlmacros import build
    from yamlmacros.src.error_highlighter import ErrorHighlighter

    error_highlighter = ErrorHighlighter(output.window, 'YAMLMacros')

    source_text = sublime.load_resource(SOURCE_PATH)

    build(
        source_text=source_text,
        destination_path=path.join(destination_path, name + '.sublime-syntax'),
        arguments=merge({
            'name': 'JS Custom - %s' % name,
            'scope': 'source.js.%s' % re.sub(r'[^\w-]', '', name.lower()),
            'file_path': SOURCE_PATH,
        }, configuration),
        error_stream=output,
        error_highlighter=error_highlighter
    )
