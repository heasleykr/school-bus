from django.db import models
from django.contrib.auth.models import AbstractUser

from schoolbus.models import Schoolbus, School

# Create your models here.


################ Objects Utilized by Users ###################
BANK_ACCOUNT_TYPES = (
    ("1", "Checking"),
    ("2", "Savings")
)

CARD_TYPES = (
    ("1", "Debit"),
    ("2", "Credit")
)

CARD_NETWORK = (
    ("1", "Visa"),
    ("2", "Mastercard"),
    ("3", "American Express"),
    ("4", "Discover")
)

class CardPayment(models.Model):
    '''
    A card form of payment associated with a User
    '''
    def __str__(self):
        return self.name

    card_type = models.CharField(max_length=36, choices=CARD_TYPES)
    card_maker = models.CharField(max_length=36, choices=CARD_NETWORK)
    card_number = models.IntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()


class BankAccount(models.Model):
    '''
    A BankAccount associated with a User
    '''
    def __str__(self):
        return self.name

    bank_name = models.CharField(max_length=36)
    routing_number = models.IntegerField()
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=36, choices=BANK_ACCOUNT_TYPES)


class Vehicle(models.Model):
    '''
    A Vehicle object attached to a Driver object
    '''
    def __str__(self):
        return self.name
    
    year = models.IntegerField()
    make = models.CharField(max_length=36)
    model = models.CharField(max_length=36)
    color = models.CharField(max_length=36)
    license_plate = models.CharField(max_length=36)
    vin = models.CharField(max_length=100)
    registartion_start_datetime = models.DateTimeField()
    registration_end_datetime = models.DateTimeField()


class InsurancePolicy(models.Model):
    '''
    An auto insurance policy attached to Driver object
    '''
    def __str__(self):
        return self.name

    insurance_carrier = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    policy_start_datetime = models.DateTimeField()
    policy_end_datetime = models.DateTimeField()
    vehicle_vin = models.CharField(max_length=100)
    address = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    state = models.CharField(max_length=36)
    zip = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)

    class Meta:
        verbose_name_plural = 'InsurancePolicies'



################ USERS ###################
class User(AbstractUser):
    '''
    A base User object.
    '''
    profile_pic = models.ImageField()
    age = models.PositiveIntegerField(null=True)
    preferred_payment_method = models.CharField(max_length=36, choices=(
        ("1", "Bank Account"),
        ("2", "Card on File")
    ))
    preferred_reimbursement_method = models.CharField(max_length=36, choices=(
        ("1", "Bank Account"),
        ("2", "Card on File")
    ))
    emergency_contact_fist_name = models.CharField(max_length=50)
    emergency_contact_last_name = models.CharField(max_length=50)
    emergency_contact_phone = models.IntegerField(null=True)


    # fk
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE, null=True)
    card_payment = models.OneToOneField(CardPayment, on_delete=models.CASCADE, null=True)



class Driver(models.Model):
    '''
    A Driver object, generated from a User object.
    Person who will drive ChildPassengers to
    authorized schools.
    '''
    
    is_authorized_for_school = models.BooleanField()
    date_authorized_start = models.DateTimeField()
    date_authorized_end = models.DateTimeField()
    authorized_date = models.DateTimeField()

    # fk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolbus = models.OneToOneField(Schoolbus, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    insurance = models.OneToOneField(InsurancePolicy, on_delete=models.CASCADE)


class ParentPassenger(models.Model):
    '''
    A ParentPassenger object, generated from a User object.
    Parent of child who will be driven to authorized
    school.
    '''
    
    is_authorized_for_school = models.BooleanField()
    date_authorized_start = models.DateTimeField()
    date_authorized_end = models.DateTimeField()
    authorized_date = models.DateTimeField()

    # fk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolbus = models.OneToOneField(Schoolbus, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class ChildPassenger(models.Model):
    '''
    A ChildPassenger object, generated from a ParentPassenger object.
    Child who will be driven to authorized school.
    '''
    
    
    is_authorized_for_school = models.BooleanField()
    date_authorized_start = models.DateTimeField()
    date_authorized_end = models.DateTimeField()
    authorized_date = models.DateTimeField()

    # fk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.OneToOneField(ParentPassenger, on_delete=models.CASCADE)
    schoolbus = models.OneToOneField(Schoolbus, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class SchoolAuthorizingPerson(models.Model):
    '''
    A SchoolAuthorizingPerson object, generated from a User object.
    Person who authorizes and authenticates Drivers and Passengers 
    for an associated School.
    '''
    
    is_authorized_for_school = models.BooleanField()
    date_authorized_start = models.DateTimeField()
    date_authorized_end = models.DateTimeField()
    authorized_date = models.DateTimeField()
    school_role = models.CharField(max_length=50)

    # fk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolbus = models.OneToOneField(Schoolbus, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)


class Trip(models.Model):
    '''
    A Trip object created when consumer requests 
    a ride. These are saved and accessed by the 
    Passenger
    '''
    def __str__(self):
        return self.name

    start_latitude = models.IntegerField()
    start_longitude = models.IntegerField()
    end_latitude = models.IntegerField()
    end_longitude = models.IntegerField()
    distance = models.IntegerField()
    loved = models.BooleanField()

    # fk
    user = models.OneToOneField(ParentPassenger, on_delete=models.CASCADE)


class Ride(models.Model):
    '''
    A unique Ride object, generated from a Trip object.
    '''
    def __str__(self):
        return self.name

    total_payment = models.IntegerField()
    duration = models.DurationField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # fk
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
