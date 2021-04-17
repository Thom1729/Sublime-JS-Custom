__all__ = ['merge']


def merge(*dicts: dict) -> dict:
    ret = {}
    for d in dicts:
        ret.update(d)
    return ret
