try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps

import inspect


def noop_handler(*args, **kwargs):
    pass


def disable_for_loaddata(signal_handler):
    for fr in inspect.stack():
        if inspect.getmodulename(fr[1]) == 'django-admin':
            return wraps(signal_handler)(noop_handler)
    return signal_handler
