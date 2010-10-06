from current_user import *

def permalink_with_prefix(func):
    """
    This works exactly like Django's permalink decorator, except it takes an
    extra prefix kwarg which is passwed along to reverse(). We also strip out
    the script prefix and make sure the supplied prefix ends with '/'.
    """
    from urlparse import urljoin
    from django.core.urlresolvers import reverse, get_script_prefix
    def inner(*args, **kwargs):
        bits = func(*args, **kwargs)
        script_prefix = get_script_prefix()
        prefix = bits[0]
        if not prefix.endswith('/'): prefix += u'/'
        bits = bits[1:]
        link = reverse(bits[0], None, *bits[1:3]).replace(script_prefix, u'', 1)
        return urljoin(prefix, link)
    return inner
