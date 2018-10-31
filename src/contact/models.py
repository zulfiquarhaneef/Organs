from django.db import models

# Create your models here.
class ContactInfo(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	message=models.CharField(max_length=500)
	def __str__(self):
		return self.name
		
	def __unicode__(self):
		return self.title
