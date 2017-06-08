from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contact_Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sph_groups'
        ordering = ('name',)
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        unique_together = ('user', 'name')

    def __str__(self):
        return "%s" % self.name

    @permalink
    def get_absolute_url(self):
        return ('group_detail', None, {
            'pk': self.pk,
        })

    @permalink
    def get_update_url(self):
        return ('group_update', None, {
            'pk': self.pk,
        })

    @permalink
    def get_delete_url(self):
        return ('group_delete', None, {
            'pk': self.pk,
        })


@python_2_unicode_compatible
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=12, help_text='start with 254xxxxxxxx')
    email = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Contact_Group, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sph_contacts'
        ordering = ('last_name', 'first_name')
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        unique_together = ('user', 'mobile')

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    @permalink
    def get_absolute_url(self):
        return ('contacts_detail', None, {
            'pk': self.pk,
        })

    @permalink
    def get_update_url(self):
        return ('contacts_update', None, {
            'pk': self.pk,
        })

    @permalink
    def get_delete_url(self):
        return ('contacts_delete', None, {
            'pk': self.pk,
        })