from .util import merge

from sublime_lib import SettingsDict


__all__ = ['get_configurations']


def get_configurations(settings: SettingsDict) -> dict:
    defaults = settings.get('defaults', {})  # type: object
    assert isinstance(defaults, dict)

    configurations = settings.get('configurations', {})  # type: object
    assert isinstance(configurations, dict)

    embed_configuration = settings.get('embed_configuration', {})  # type: object
    assert isinstance(embed_configuration, dict)

    return {
        name: merge(defaults, config)
        for name, config in merge({'~embed': embed_configuration}, configurations).items()
    }
