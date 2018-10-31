from django.db import models


class DoctorInfo(models.Model):
	docname=models.CharField('Doctor Name',max_length=200)
	hosname=models.CharField('Hospital Name', max_length=400)
	address=models.CharField('Address',max_length=200)
	phone=models.CharField('Contact Number',max_length=200)
	email=models.CharField('E-mail',max_length=200)
	username=models.CharField('Username',max_length=200)
	password=models.CharField('Password',max_length=200)
		
	def __str__(self):
		return self.docname

