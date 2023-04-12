from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

from phonenumber_field.formfields import PhoneNumberField

# no authentication here yet.
class CustomUserCreationForm(UserCreationForm):
    emergency_contact_phone = PhoneNumberField()
    """Form to create the User model"""
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'first_name',
            'last_name',
            'username',
            'email',
            'age',
            'emergency_contact_fist_name',
            'emergency_contact_last_name',
            'emergency_contact_phone',
        )


class CustomUserChangeForm(UserChangeForm):
    """Form to update a User Account"""
    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email',)


class CustomUserLoginForm(AuthenticationForm):
    """Form to login to User Account"""
    # class Meta(AuthenticationForm):
