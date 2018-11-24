import sublime
from functools import partial


__all__ = ['defer', 'defer_each']


def defer(function, *args, **kwargs):
    sublime.set_timeout_async(partial(function, *args, **kwargs), 0)


def defer_each(function, iterable):
    iterator = iter(iterable)

    def _iteration(value):
        function(value)
        _schedule_next()

    def _schedule_next():
        try:
            value = next(iterator)
        except StopIteration:
            return

        defer(_iteration, value)

    _schedule_next()
