from django.conf import settings
from django.http import HttpResponseServerError, HttpResponseForbidden
from django.template import Context, loader


def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({'MEDIA_URL':
                                                     settings.MEDIA_URL})))


def server_forbidden(request, template_name='403.html'):
    """
    403 error handler.

    Templates: `403.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 403.html template.
    return HttpResponseForbidden(t.render(Context({'MEDIA_URL':
                                                   settings.MEDIA_URL})))
