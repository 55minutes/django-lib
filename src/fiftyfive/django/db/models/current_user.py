from django.db import models
from django.contrib.auth.models import User

import registration

__all__ = ('CurrentUserField',)

class CurrentUserField(models.ForeignKey):
    def __init__(self, **kwargs):
        super(CurrentUserField, self).__init__(User, null=True, **kwargs)

    def contribute_to_class(self, cls, name):
        super(CurrentUserField, self).contribute_to_class(cls, name)
        registry = registration.FieldRegistry()
        registry.add_field(cls, self)
