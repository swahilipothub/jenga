from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext as _


class Contact_Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'groups'
        ordering = ('name',)
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        unique_together = ('user', 'name')

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('group_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('group_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('group_delete', args=[self.pk])


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=13, help_text='start with 254xxxxxxxx')
    category = models.ManyToManyField(Contact_Group)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contacts'
        ordering = ('full_name', )
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        unique_together = ('user', 'mobile')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('contacts_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('contacts_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('contacts_delete', args=[self.pk])
