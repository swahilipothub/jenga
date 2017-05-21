from __future__ import unicode_literals

from django.db import models



class Contact_Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13, unique =True)
    id_number = models.CharField(max_length=8, unique=True)
    category = models.ForeignKey(Contact_Group)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #   return ' '.join([self.first_name, self.last_name,])

    def __str__(self):
        return self.mobile

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})