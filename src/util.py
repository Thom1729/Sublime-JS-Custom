def coalesce(*args):
    return next((x for x in args if x is not None), None)

def merge(*dicts):
    ret = {}
    for d in dicts:
        ret.update(d)
    return ret
