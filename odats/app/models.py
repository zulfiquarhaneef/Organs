from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from background_task import background

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

#MALE, FEMALE = range(2)
GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

BLOODGROUPS = (
	('A+', 'A+'),
	('A-', 'A-'),
	('B+', 'B+'),
	('B-', 'B-'),
	('AB+', 'AB+'),
	('AB-', 'AB-'),
	('O+', 'O+'),
	('O-', 'O-')
)


#HEART, LUNGS, KIDNEY, LIVER, TISSUE, PANCREAS, CORNEAS,EYES = range(8)
ORGAN = (
    ('HEART', 'HEART'),
    ('LUNGS', 'LUNGS'),
    ('KIDNEY', 'KIDNEY'),
    ('LIVER', 'LIVER'),
    ('TISSUE', 'TISSUE'),
    ('PANCREAS', 'PANCREAS'),
    ('CORNEAS', 'CORNEAS'),
    ('EYES','EYES'),
)

#User models:

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

#Organs :

#Organ - a model to represent an organ
class Organ(models.Model):
	type_of_organ = models.CharField('Organ', choices=ORGAN, default='HEART', max_length=15)
	bloodgroup = models.CharField('BGroup', choices=BLOODGROUPS, default='B+', max_length=10)
	pub_date = models.DateTimeField('datetime')
	expired = models.BooleanField(default=False)
	assigned = models.BooleanField(default=False)
	donor = models.ForeignKey(User, related_name='donor', default=0)
	
	def __str__(self):
		return self.type_of_organ + ' - ' + self.bloodgroup

#Hospital:
class Hospital(models.Model):
	hospital_name = models.CharField(max_length=200)
	hospital_address = models.CharField(max_length=400)
	licno = models.CharField(max_length=200)
	certificate = models.CharField(max_length=200)
	district = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	nameofgm = models.CharField(max_length=200)
	departments = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	website = models.CharField(max_length=300)
	def __str__(self):
		return self.hospital_name

# Doctor - model for doctor:
class Doctor(models.Model):
	doc_name=models.CharField('Doctor Name',max_length=200)
	hospital=models.ForeignKey(Hospital, related_name='hospital')
	address=models.CharField('Address',max_length=200)
	phone=models.CharField('Contact Number',max_length=200)
	user = models.ForeignKey(User, related_name="doctor_user", default=0)
		
	def __str__(self):
		return self.doc_name


#Donation request
class DonateOrgan(models.Model):
	full_name = models.CharField(max_length=200)
	Address = models.CharField(max_length=500)
	District = models.CharField(max_length=200)
	Pincode = models.CharField(max_length=200)
	State = models.CharField(max_length=200)
	Gender = models.CharField(choices=GENDER, max_length=10)
#	Blood_group=models.CharField(max_length=200)
	Relative_name = models.CharField(max_length=200)
	Relationship = models.CharField(max_length=200)
	Contact = models.CharField(max_length=200)
	organ = models.ForeignKey(Organ, related_name='organ')
	
	def __str__(self):
		return self.full_name

#DOctor requested organs
class DoctorRequestOrgan(models.Model):
	Doctor = models.ForeignKey(User, related_name='doctor')
	Hospitalname = models.ForeignKey(Hospital, related_name='hospitalname')
	Patientname = models.CharField(max_length=200)
	Patienttype = models.CharField(max_length=200)
#	Bloodgroup = models.CharField(max_length=200)
	organs = models.ForeignKey(Organ, related_name='organs')
	Reason=models.CharField(max_length=300)
	Description=models.CharField(max_length=500)
	Contactnumber=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)
	def __str__(self):
		return self.Doctor.full_name
		
	def __unicode__(self):
		return self.Doctor

######################################

class AssingedOrgans(models.Model):
    organ = models.ForeignKey(Organ, related_name='assigned_organ')
    assigned_to = models.ForeignKey(User, related_name='assigned_to')

    def __str__(self):
        return self.organ.__str__()

#Proxy model for dashboard features in admin
class OdatsSummary(AssingedOrgans):
	class Meta:
		proxy = True
		verbose_name = 'ODATS - Stats'
		verbose_name_plural = 'ODATS - Stats'


@background()
def updateOrgans():
	organs = Organ.objects.exclude(expired=True).exclude(assigned=True)
	for organ in organs:
		delta = (timezone.make_aware(datetime.now(), timezone.get_current_timezone()) - organ.pub_date)
		if timedelta(hours=6) > delta:
			print(organ.__str__() + "is Still fresh!")
		else:
			print(organ.__str__() + "is wasted after ")
			print(timedelta(hours=6))
			organ.expired = True
			organ.save()
updateOrgans(repeat=120)
#updateOrgans()

