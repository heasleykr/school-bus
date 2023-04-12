from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.views.generic import CreateView, FormView
from django.db import models
from .models import User


# always take in request param, always returns response or redirect
# 2 ways: Func based, classed-based (abstraction)
# def login(request):
#     return render(request, 'home.html')

# Using view object instead of definition?

# Signup View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def login_view(request):
    args = {'form': CustomUserLoginForm}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            args['form_errors'] = True
            return render(request, 'registration/login.html', args)
    else:
        return render(request, 'registration/login.html', args)


# TODO: Make POST / GET difference
def logout_view(request):
    # modifying server state should not be done through
    # a GET. These are read only 
    # anytime you handle a post on the server, you need a redirect.
    if request.method == 'POST':
        # if Post... log out, then redirect to logout view
        if request.user.is_active:
            logout(request)
            return redirect('logout')
    else:
        return render(request, 'registration/logout.html')


#TODO: complete this
class PasswordChangeView(FormView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('home')


# TODO: renders User's indox messages
def inbox(request):
    # TODO: query Mesages, add Models
    return render(request, 'user/inbox.html')


# TODO: renders User's past trips
def trips(request):
    # TODO: query Trips
    return render(request, 'user/trips.html')