from sublime_lib import NamedSettingsDict


__all__ = ['get_settings']


SETTINGS = None


def get_settings() -> NamedSettingsDict:
    global SETTINGS
    if SETTINGS is None:
        SETTINGS = NamedSettingsDict('JS Custom')
    return SETTINGS
