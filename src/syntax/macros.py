from ruamel.yaml import SafeLoader
from yamlmacros import get_loader

from sublime_lib import ResourcePath


__all__ = ['get_extensions', 'do_suffix']


def parse_documents(text):
    loader = SafeLoader(text)
    composer = loader.composer
    while composer.check_node():
        yield composer.get_node()


def list_extensions(path):
    for path in path.rglob('*.syntax-extension'):
        parsed_documents = list(parse_documents(path.read_text()))

        metadata = {
            'name': path.stem,
            'macros_root': str(path.parent)
        }

        if len(parsed_documents) == 1:
            value_document = parsed_documents[0]
        else:
            metadata_document, value_document = parsed_documents

            constructor = get_loader(macros_root=str(path.parent)).constructor
            given_metadata = constructor.construct_document(parsed_documents[0])
            if given_metadata:
                metadata.update(**given_metadata)

        yield (metadata, value_document)


def get_extensions(path):
    arguments = (yield).context
    ret = []

    extensions = list(list_extensions(ResourcePath(path)))

    for extension in extensions:
        metadata, extension_value = extension

        options = arguments.get(metadata['name'])

        if options is not None and options is not False:
            constructor = get_loader(macros_root=metadata['macros_root']).constructor

            if 'legacy_argument' in metadata:
                options = {
                    metadata['legacy_argument']: options
                }
            elif not isinstance(options, dict):
                default_argument = metadata.get('default_argument')
                if default_argument:
                    options = {default_argument: options}
                else:
                    options = {}

            with constructor.set_context(**options):
                result = constructor.construct_document(extension_value)
                ret.append(result)

    return ret

import re

JS_EXPR = re.compile(r'\.js(?:$|(?=[.\s]))')

def do_suffix(definition):
    arguments = (yield).context

    suffix = arguments.get('suffix', None)
    if suffix:
        def replace_suffix(string):
            return JS_EXPR.sub('.' + suffix, string)

        def patch_context(context):
            for rule in context:
                for key in ('scope', 'meta_scope', 'meta_content_scope'):
                    if key in rule:
                        rule[key] = replace_suffix(rule[key])

                if 'captures' in rule:
                    for index, capture_scope in rule['captures'].items():
                        rule['captures'][index] = replace_suffix(capture_scope)

                for key in ('push', 'set'):
                    if key in rule:
                        if (
                            isinstance(rule[key], list) and
                            len(rule[key])
                        ):
                            if isinstance(rule[key][0], dict):
                                patch_context(rule[key])
                            else:
                                for child in rule[key]:
                                    if isinstance(child, list):
                                        patch_context(child)

        for name, context in definition['contexts'].items():
            patch_context(context)

    return definition
