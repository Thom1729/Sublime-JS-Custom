__all__ = ['merge']


def merge(*dicts):
    ret = {}
    for d in dicts:
        ret.update(d)
    return ret
