"""Testing1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from doclogin.views import doclogin_page

from accounts.views import LoginView, RegisterView, guest_register_view
from requestOrgan.views import Organ_request,proced_request_organ
from DonationRequest.views import donation_page,donating_form
from addhospital.views import hospital_registration,proced_hospital
from adddoctor.views import doctor_registration,proced_doctor
from contact.views import contact_page,contact_click
from .views import home_page,about_page,services_page,doctorlogin,user_page,doctor_page,doctorabout_page,doctorcontact_page,doctorservices_page,userservices_page,userabout_page,usercontact_page
from doctorrequest.views import docrequest_page,drequest_page_click

urlpatterns = [
    url(r'^$',home_page, name="home"),
    url(r'^about/', about_page, name="about"),
    url(r'^userhome/', user_page, name="userhome"),
    url(r'^userabout/', userabout_page, name="userabout"),
    url(r'^usercontact/', usercontact_page, name="usercontact"),
    url(r'^userservices/', userservices_page, name="userservices"),
    url(r'^doctor/login/', doclogin_page , name="doclogin"),
    url(r'^doctorlogin', doctorlogin, name="doctorlogin"),
    url(r'^doctor/adddoctor', doctor_registration, name="doctorregstration"),
    url(r'^procedoctor/', proced_doctor),
    url(r'^doctor/', doctor_page, name="doctorhome"),
    url(r'^doctorabout/', doctorabout_page, name="doctorabout"),
    url(r'^doctorcontact/', doctorcontact_page, name="doctorcontact"),
    url(r'^doctorservices/', doctorservices_page, name="doctorservices"),
    url(r'^contact/',contact_page, name="contact"),
    url(r'^contact_click/',contact_click),
    url(r'^donation/requestOrgan/', Organ_request, name="organrequest"),
    url(r'^donation/procedrequest/',drequest_page_click),
    url(r'^hospitalregistration/', hospital_registration),
    url(r'^procedhospital/', proced_hospital),
    url(r'^doctor/organrequest_click', drequest_page_click),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^donation/donation/', donation_page, name='donation' ),
    url(r'^services/services/', services_page, name='services'),
    url(r'^donation/donation_form', donating_form),
    url(r'^requestdoc/',docrequest_page, name='requestdoc'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
