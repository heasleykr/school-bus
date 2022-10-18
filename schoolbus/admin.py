from django.contrib import admin
from schoolbus.models import School, Schoolbus
# Register your models here.


@admin.register(Schoolbus)
class SchoolbusAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

