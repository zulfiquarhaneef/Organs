from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^register/$', views.RegisterView.as_view(), name='register'),
	url(r'^register/guest/$', views.guest_register_view, name='guest_register'),
]