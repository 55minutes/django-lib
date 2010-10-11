from django.contrib.localflavor.us import models

class USStateField(models.USStateField): 
    def formfield(self, **kwargs): 
        from forms import USStateSelect
        defaults = {'widget': USStateSelect(render_empty=self.blank,
                                            empty_label=u'Select a state')}
        defaults.update(kwargs)
        return super(USStateField, self).formfield(**defaults)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        [], ['^fiftyfive\.django\.contrib\.localflavor\.us\.models\.USStateField'])
except ImportError:
    pass

