from django.contrib import admin
from django.urls import path

from .views import home, request_ride, all_schools, approved_schools


urlpatterns = [
    # when url , execute func
    path('', home, name='home'),
    path('request_ride', request_ride, name='request_ride'),
    path('approved_schools', approved_schools, name='approved_schools'),
    path('all_schools', all_schools, name='all_schools')
]
