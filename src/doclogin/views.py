from django.shortcuts import render

# Create your views here.
def doclogin_page(request):
	return render(request,"signup/doclogin.html")
