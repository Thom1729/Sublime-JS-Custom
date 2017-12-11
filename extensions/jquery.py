from YAMLMacros.lib.extend import Operation

def find_rule(condition, node):
    if isinstance(list, node):
        for item in node: yield from find_rule(condition, item)
    elif isinstance(dict, node):
        if condition(node):
            yield node
        else:
            for key, item in node.items():
                yield from find_rule(condition, item)

class StripJquery(Operation):
    def apply(self, base):
        print(list(find_rule(
            lambda node: True,
            base
        )))
        return base

def strip_jquery(*args):
    return StripJquery(None)
