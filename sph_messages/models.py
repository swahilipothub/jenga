from __future__ import unicode_literals
from django.db.models import permalink
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from contacts.models import Contact


@python_2_unicode_compatible
class Sms(models.Model):
	to = models.CharField(max_length=1040)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

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