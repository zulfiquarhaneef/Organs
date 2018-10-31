from django.shortcuts import render
from .models import DoctorRequestOrgan
# Create your views here.
def docrequest_page(request):
	return render(request,"DoctorRequestOrgan/doctorrequestorgan.html",{})

def drequest_page_click(request):
	print("form submited")
	dname=request.POST["dname"]
	hname=request.POST["hname"]
	pname=request.POST["pname"]
	ptype=request.POST["ch1"]
	bggroup=request.POST["bggroup"]
	rorgans=request.POST["organs"]
	reason=request.POST["reason"]
	description=request.POST["description"]
	contact=request.POST["contact"]
	email=request.POST["email"]
	drequest=DoctorRequestOrgan(Doctorname=dname,
		Hospitalname=hname,
		Patientname=pname,
		Patienttype=ptype,
		Bloodgroup=bggroup,
		Organs=rorgans,
		Description=description,
		Contactnumber=contact,
		Email=email)
	drequest.save()
	return render(request,"DoctorRequestOrgan/doctorrequestorgan.html")
