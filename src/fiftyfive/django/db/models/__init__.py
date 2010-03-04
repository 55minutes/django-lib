from current_user import *

def permalink_with_prefix(func):
    """
    This works exactly like Django's permalink decorator, except it takes an
    extra prefix kwarg which is passwed along to reverse().
    """
    from django.core.urlresolvers import reverse
    def inner(*args, **kwargs):
        bits = func(*args, **kwargs)
        return reverse(bits[0], None, *bits[1:])
    return inner
