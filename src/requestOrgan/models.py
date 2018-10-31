from django.db import models

# Create your models here.

class OrganReq(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	address=models.CharField(max_length=400)
	district=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	pincode=models.CharField(max_length=200)
	gender=models.CharField(max_length=200)
	bgroup=models.CharField(max_length=200)
	contact=models.CharField(max_length=200)
	requestOrg=models.CharField(max_length=200)
	reason=models.CharField(max_length=200)
	def __str__(self):
		return self.firstname

