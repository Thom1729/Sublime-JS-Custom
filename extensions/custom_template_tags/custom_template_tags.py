def get_options(options):
    if (
        isinstance(options, dict) and
        len(options) > 0 and
        all(
            isinstance(value, str)
            for value in options.values()
        )
    ):
        return {
            'tags': options
        }
    else:
        return options
