from .util import merge


__all__ = ['get_configurations']


def get_configurations(settings):
    defaults = settings.get('defaults', {})
    return {
        name: merge(defaults, config)
        for name, config in merge(
            {'~embed': settings.get('embed_configuration', {})},
            settings.get('configurations', {})
        ).items()
    }
