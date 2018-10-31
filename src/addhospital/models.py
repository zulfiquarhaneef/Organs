from django.db import models

# Create your models here.

class HospitalInfo(models.Model):
	hosname=models.CharField(max_length=200)
	hosaddress=models.CharField(max_length=400)
	licno=models.CharField(max_length=200)
	certificate=models.CharField(max_length=200)
	district=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	nameofgm=models.CharField(max_length=200)
	departments=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	contact=models.CharField(max_length=200)
	website=models.CharField(max_length=300)
	def __str__(self):
		return self.hosname

