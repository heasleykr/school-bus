from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Driver,
    ParentPassenger,
    ChildPassenger,
    SchoolAuthorizingPerson,
    CardPayment,
    BankAccount,
    Vehicle,
    InsurancePolicy
)

admin.site.register(User, UserAdmin)


################  Users ###################
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(ParentPassenger)
class ParentPassengerAdmin(admin.ModelAdmin):
    pass

@admin.register(ChildPassenger)
class ChildPassengerAdmin(admin.ModelAdmin):
    pass

@admin.register(SchoolAuthorizingPerson)
class SchoolAuthorizingPersonAdmin(admin.ModelAdmin):
    pass


################ Objects Utilized by Users ###################
@admin.register(CardPayment)
class CardPaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    pass