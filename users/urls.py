from django.contrib import admin
from django.urls import path

from .views import SignUpView, logout_view, PasswordChangeView, inbox, trips, login_view


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('passsword_change/', PasswordChangeView.as_view(), name='password_change'),
    path('inbox/', inbox, name='inbox'),
    path('trips/', trips, name='trips')
    
    # TODO: Set views
    # users/ password_change/done/ [name='password_change_done']
    # users/ password_reset/ [name='password_reset']
    # users/ password_reset/done/ [name='password_reset_done']
    # users/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # users/ reset/done/ [name='password_reset_complete']

]