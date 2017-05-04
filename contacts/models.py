from __future__ import unicode_literals

from django.db import models

CATEGORY = (('Tech', 'Tech'), ('Arts', 'Arts'), )


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13, unique=True)
    id_number = models.CharField(max_length=8, unique=True)
    categogry = models.CharField(choices=CATEGORY, max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return ' '.join([self.first_name, self.last_name,])

    def __str__(self):
        return self.mobile

class Contact_Group(models.Model):
    name = models.CharField(max_length=255)
    contacts = models.ManyToManyField(Contact)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sms(models.Model):
    group = models.ForeignKey(Contact_Group)
    sms = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
