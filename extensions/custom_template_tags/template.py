from yamlmacros.lib.include import include_resource

def eval(resource):
    print('RESOURCE', resource)
    x = yield from include_resource(resource)
    print('VALUE', x)
    return x
