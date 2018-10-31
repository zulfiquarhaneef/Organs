from django.shortcuts import render

# Create your views here.

from .models import HospitalInfo

# Create your views here.
def hospital_registration(request):
	return render(request,"Hospital/addhospital.html")


def proced_hospital(request):
	print("form submitted")
	hname=request.POST['hname']
	haddress=request.POST['address']
	hlic=request.POST['lic']
	hdistrict=request.POST['district']
	hstate=request.POST['state']
	hcontact=request.POST['contact']
	hgmname=request.POST['gmname']
	hemail=request.POST['email']
	hdepartments=request.POST['departments']
	hcertificate=request.POST['c1']
	hwebsite=request.POST['website']
	hos_info=HospitalInfo(hosname=hname,
		hosaddress=haddress,
		licno=hlic,
		district=hdistrict,
		state=hstate,
		nameofgm=hgmname,
		departments=hdepartments,
		contact=hcontact,
		email=hemail,
		website=hwebsite)
	hos_info.save()
	return render(request,"Hospital/addhospital.html")