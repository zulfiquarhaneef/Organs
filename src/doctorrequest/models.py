from django.db import models

# Create your models here.
class DoctorRequestOrgan(models.Model):
	Doctorname=models.CharField(max_length=200)
	Hospitalname=models.CharField(max_length=200)
	Patientname=models.CharField(max_length=200)
	Patienttype=models.CharField(max_length=200)
	Bloodgroup=models.CharField(max_length=200)
	Organs=models.CharField(max_length=200)
	Reason=models.CharField(max_length=300)
	Description=models.CharField(max_length=500)
	Contactnumber=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)
	def __str__(self):
		return self.Doctorname
		
	def __unicode__(self):
		return self.Doctorname
