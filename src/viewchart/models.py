from django.db import models

# Create your models here.

MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

HEART, LUNGS, KIDNEY, LIVER, TISSUE, PANCREAS, CORNEAS,EYES = range(8)
DONATE = (
    (HEART, 'HEART'),
    (LUNGS, 'LUNGS'),
    (KIDNEY, 'KIDNEY'),
    (LIVER, 'LIVER'),
    (TISSUE, 'TISSUE'),
    (PANCREAS, 'PANCREAS'),
    (CORNEAS, 'CORNEAS'),
    (EYES,'EYES'),
)

class DonationReques(models.Model):
    Firstname=models.CharField('First Name',max_length=200)
    Lastname=models.CharField('Last Name',max_length=200)
    Address=models.CharField(max_length=500)
    District=models.CharField(max_length=200)
    Pincode=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Gender=models.PositiveSmallIntegerField('Gender',choices=GENDER,default=MALE)
    Bloodgroup=models.CharField('Bloodgroup', max_length=200 )
    Relative_name=models.CharField(max_length=200)
    Relationship=models.CharField(max_length=200)
    Contact=models.CharField(max_length=200)
    Donate=models.PositiveSmallIntegerField('Donate',choices=DONATE,default=HEART)
    
    
    def __str__(self):
        return self.Firstname

    class Meta:
        verbose_name = ('DonationReques')
