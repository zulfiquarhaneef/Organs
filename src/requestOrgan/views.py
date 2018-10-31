from django.shortcuts import render

# Create your views here.
from .models import OrganReq


def Organ_request(request):
	return render(request,"Donation/requestOrgan.html")


def proced_request_organ(request):
	print("submitted")
	rfirstname=request.POST['firstname']
	rlastname=request.POST['lastname']
	raddress=request.POST['address']
	rdistrict=request.POST['district']
	rpincode=request.POST['pincode']
	rstate=request.POST['state']
	rbgroup=request.POST['bgroup']
	rgender=request.POST['gender']
	rcontact=request.POST['contact']
	rch1=request.POST['ch1']
	rreason=request.POST['reason']
	request_organ=OrganRequest(firstname=rfirstname,
		lastname=rlastname,
		address=raddress,
		district=rdistrict,
		pincode=rpincode,
		state=rstate,
		bgroup=rbgroup,
		gender=rgender,
		contact=rcontact,
		requestOrg=rch1,
		reason=rreason)
	request_organ.save()
	print("rchoice")
	return render(request,"Donation/requestOrgan.html")