from django.db import models


SCHOOL_TYPES = (
    ("1", "Kindergarten"),
    ("2", "Preschool"),
    ("3", "K-12"),
    ("4", "Middle School"),
    ("5", "High School")
)


class Schoolbus(models.Model):
    '''
    A school district object
    '''
    def __str__(self):
        return self.name
    # creates pk for you
    # null vs blank
    # before: add views django-admin..see database columns, build models out
    # next time: moving data progrmatically in CLI
    name = models.CharField(max_length=36)
    district = models.CharField(max_length=36)
    community = models.CharField(max_length=36)
    county = models.CharField(max_length=36)
    state = models.CharField(max_length=36)

    class Meta:
        verbose_name_plural = 'Schoolbuses'


class School(models.Model):
    '''
    A school object attached to a SchoolBus object
    '''
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=36)
    school_type = models.CharField(max_length=36, choices=SCHOOL_TYPES)
    school_bus = models.ForeignKey(Schoolbus, on_delete=models.CASCADE)
    address = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    state = models.CharField(max_length=36)
    zip = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    principle = models.CharField(max_length=36)

