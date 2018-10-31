from django.shortcuts import render
from .models import ContactInfo

# Create your views here.
def contact_page(request):
	return render(request,"contact/view.html")

def contact_click(request):
	print("form submited")
	mname=request.POST["name"]
	memail=request.POST["email"]
	msubject=request.POST["subject"]
	mmessage=request.POST["msg"]
	contact_info=ContactInfo(name=mname,email=memail,subject=msubject,message=mmessage)
	contact_info.save()
	return render(request,"contact/view.html")