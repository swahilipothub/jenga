from __future__ import unicode_literals

from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from contacts.models import Contact_Group


class Sms(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Contact_Group, on_delete=models.CASCADE)
	message = models.TextField()
	number = models.CharField(max_length=13)
	status = models.CharField(max_length=50)
	messageId = models.CharField(max_length=256)
	cost = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'messages'

	def __str__(self):
		return "%s" % self.message

	def get_absolute_url(self):
		return reverse('message_detail', args=[self.pk])

	def get_update_url(self):
		return reverse('message_update', args=[self.pk])

	def get_delete_url(self):
		return reverse('message_delete', args=[self.pk])
