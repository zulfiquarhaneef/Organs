from django.shortcuts import render

from .models import DoctorInfo

# Create your views here.
def doctor_registration(request):
	return render(request,"Doctor/adddoctor.html")


def proced_doctor(request):
	print("form submitted")
	dname=request.POST['dname']
	dhname=request.POST['hosname']
	daddress=request.POST['daddress']
	dphone=request.POST['dphone']
	demail=request.POST['demail']
	dusername=request.POST['username']
	dpassword=request.POST['password']
	doc_info=DoctorInfo(
		docname=dname,
		hosname=hosname,
		address=daddress,
		phone=dphone,
		email=demail,
		username=dusername,
		password=dpassword )
	doc_info.save()
	return render(request,"Doctor/adddoctor.html")
