from django.shortcuts import render
from .models import DonationReq
# Create your views here.
def donation_page(request):
	return render(request,"Donation/donation.html")

def donating_form(request):
	print("submitted")
	dfirstname=request.POST['firstname']
	dlastname=request.POST['lastname']
	daddress=request.POST['address']
	ddistrict=request.POST['district']
	dpincode=request.POST['pincode']
	dstate=request.POST['state']
	dgender=request.POST['gender']
	dbgroup=request.POST['bgroup']
	drname=request.POST['rname']
	drelationship=request.POST['realationship']
	dcontact=request.POST['contact']
	ddonate=request.POST['organs']
	
	donation_req=DonationReq(Firstname=dfirstname,
		Lastname=dlastname,
		Address=daddress,
		District=ddistrict,
		Pincode=dpincode,
		State=dstate,
		Gender=dgender,
		Blood_group=dbgroup,
		Relative_name=drname,
		Relationship=drelationship,
		Contact=dcontact,
		Donate=ddonate	)
	donation_req.save()
	return render(request,"Donation/donation.html")