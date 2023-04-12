from django.shortcuts import render
from django.http import HttpResponse
from .models import School
# Create your views here.

# always take in request param, always returns response or redirect
# 2 ways: Func based, classed-based (abstraction)


# default home view
def home(request):
    context = {'home_view': 'homeView'}
    if request.user.is_authenticated:
        # update background image
        context = {'home_view': 'homeViewLoggedIn'}
    return render(request, 'home.html', context=context)


# map view when ParentPassenger requests ride
def request_ride(request): 
    return render(request, 'request_ride.html')


# shows available schools
def all_schools(request):
    # query 
    schools = School.objects.all()
    print(schools)
    print(request.method)
    return render(request, 'school_list.html', {'schools': schools})


# renders User's approved schools
def approved_schools(request):
    # query 
    schools = School.objects.all()
    print(schools)
    print(request.method)
    return render(request, 'user/approved_schools.html', {'schools': schools})