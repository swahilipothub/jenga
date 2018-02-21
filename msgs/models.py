from __future__ import unicode_literals

from django.db.models import permalink
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible

from contacts.models import Contact_Group


@python_2_unicode_compatible
class Sms(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Contact_Group)
	message = models.TextField()
	number = models.CharField(max_length=13)
	status = models.CharField(max_length=50)
	messageId = models.CharField(max_length=10)
	cost = models.CharField(max_length=6)
	created = models.DateTimeField(auto_now_add=True)	

	class Meta:
		db_table = 'messages'

	def __str__(self):
		return "%s" % self.message

	@permalink
	def get_absolute_url(self):
		return ('message_detail', None, {
            'pk': self.pk,
        })

	@permalink
	def get_update_url(self):
		return ('message_update', None, {
	        'pk': self.pk,
	    })

	@permalink
	def get_delete_url(self):
		return ('message_delete', None, {
	        'pk': self.pk,
	    })	