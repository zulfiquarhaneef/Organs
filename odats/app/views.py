from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm, RequestOrganForm
from .models import GuestEmail

# Create your views here.

def index(request):
	context = {}
	return render(request, 'app/index.html', context)

def about(request):
	return HttpResponse("About page")

@login_required
def donate(request):
	return HttpResponse("Donate page")


class ReqOrganView(FormView):
	form_class = RequestOrganForm
	template_name = 'app/reqorgan.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.Doctor = self.request.user
		form.instance.organs.assigned = True
		form.instance.organs.save()
		form.save()
		return HttpResponseRedirect(self.get_success_url())



#User account registration views:

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email       = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")



class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'app/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or '/'
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if user.is_admin:
            	return redirect("/admin")
            return redirect(redirect_path)
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'app/signup.html'
    success_url = '/login'