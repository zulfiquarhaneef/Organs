from django.conf.urls import url

from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^about/', views.about, name='about'),
	url(r'^donate/', views.donate, name='donate'),
	url(r'^reqorgan/', views.reqorgan, name='reqorgan'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
	url(r'^register/$', views.RegisterView.as_view(), name='register'),
]