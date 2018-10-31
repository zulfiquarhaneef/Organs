from django.db import models

# Create your models here.
class DonationReq(models.Model):
	Firstname=models.CharField(max_length=200)
	Lastname=models.CharField(max_length=200)
	Address=models.CharField(max_length=500)
	District=models.CharField(max_length=200)
	Pincode=models.CharField(max_length=200)
	State=models.CharField(max_length=200)
	Gender=models.CharField(max_length=200)
	Blood_group=models.CharField(max_length=200)
	Relative_name=models.CharField(max_length=200)
	Relationship=models.CharField(max_length=200)
	Contact=models.CharField(max_length=200)
	Donate=models.CharField(max_length=200 )
	
	def __str__(self):
		return self.Firstname
