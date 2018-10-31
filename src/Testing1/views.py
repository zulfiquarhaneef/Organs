from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,get_user_model

def home_page(request):
	context={
	"title":"Home Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"index/homepage.html",context)
	
def doctorlogin(request):
	return render(request,"signup/doclogin.html",{})

def user_page(request):
	context={
	"title":"Home Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"index/userhome.html",context)

def doctor_page(request):
	context={
	"title":"Home Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"index/doctorhome.html",context)


def about_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"aboutus/about.html",context)

def services_page(request):
   return render(request,"services/services.html",{})

def doctorabout_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"DoctorRequestOrgan/doctorabout.html",context)

def doctorcontact_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"DoctorRequestOrgan/doctorcontact.html",context)

def doctorservices_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"DoctorRequestOrgan/doctorservices.html",context)





def userservices_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"user/userservices.html",context)

def userabout_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"user/userabout.html",context)

def usercontact_page(request):
	context={
	"title":"about Page",
	"content":"Hello Iam From Home Page"
	}
	return render(request,"user/usercontact.html",context)
