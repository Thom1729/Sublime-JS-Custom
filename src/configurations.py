from .util import merge

def get_configurations(settings):
    defaults = settings.get('defaults', {})
    return {
        name: merge(defaults, config)
        for name, config in merge(
            { '~embed': settings.get('embed_configuration', {}) },
            settings.get('configurations', {})
        ).items()
    }
