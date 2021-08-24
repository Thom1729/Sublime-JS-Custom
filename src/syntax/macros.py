from ruamel.yaml import SafeLoader
from yamlmacros import get_loader

from sublime_lib import ResourcePath


__all__ = ['get_extensions']


def parse_documents(text):
    loader = SafeLoader(text)
    composer = loader.composer
    while composer.check_node():
        yield composer.get_node()


def get_extensions(base, configuration):
    print(base, configuration)
    names = [
        name for name, options in configuration.items()
        if options is not None
        and options is not False
    ]

    # Hack hacky hack to make sure that JSX is after TypeScript
    if 'jsx' in names and 'typescript' in names:
        names.remove('jsx')
        names.remove('typescript')
        names.extend(['typescript', 'jsx'])

    return [
        eval_extension(load_extension(ResourcePath(base), name), configuration[name])
        for name in names
    ]


def load_extension(base, name):
    resources = base.rglob("{}.syntax-extension".format(name))
    if len(resources) == 0:
        raise ValueError("Could not find syntax extension named {!r}.".format(name))
    elif len(resources) > 1:
        raise ValueError("Found more than one syntax extension named {!r}.".format(name))
    
    path = resources[0]

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

    return (metadata, value_document)


def eval_extension(extension, options):
    metadata, extension_value = extension

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
        result = convert_extension(result)
        return result


def convert_extension(extension):
    from yamlmacros.lib.extend import merge, prepend

    if 'extends' in extension:
        del extension['extends']
        del extension['version']
        del extension['name']
        del extension['file_extensions']
        del extension['scope']

    if 'variables' in extension:
        extension['variables'] = merge(extension['variables'])

    if 'contexts' in extension:
        for name, context in list(extension['contexts'].items()):
            if len(context) and context[0].get('meta_prepend', False):
                extension['contexts'][name] = prepend(*context[1:])

        extension['contexts'] = merge(extension['contexts'])

    return merge(extension)
