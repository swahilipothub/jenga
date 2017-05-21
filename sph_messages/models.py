from __future__ import unicode_literals

from django.db import models

from contacts.models import Contact

class Sms(models.Model):
	to = models.CharField(max_length=1050)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)