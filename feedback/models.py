from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Feedback(models.Model):
	name = models.CharField(max_length=200)
	contact_email = models.EmailField(max_length=70)
	contact_phone = models.CharField(max_length=40,blank=True,null=True)
	feedback_text = models.TextField(max_length=500)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.name