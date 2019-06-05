from ruamel.yaml import SafeLoader
from yamlmacros import get_loader

from sublime_lib import ResourcePath


__all__ = ['get_extensions']


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

            if not isinstance(options, dict):
                default_argument = metadata.get('default_argument')
                if default_argument:
                    options = {default_argument: options}
                else:
                    options = {}

            with constructor.set_context(**options):
                result = constructor.construct_document(extension_value)
                ret.append(result)

    return ret
