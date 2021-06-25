from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Language(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=255)
    acronym = models.CharField(unique=True, max_length=255)
    eula = models.TextField()
    strings = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        # managed = False
        db_table = 'edubox_languages'
        app_label = 'languages'
        default_permissions = ('add', 'change', 'delete', 'view')
        verbose_name = _('Language')