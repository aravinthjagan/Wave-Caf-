from django.db import models

# Create your models here.

PLAN_CHOICES = (
    ('afternoon','AFTERNOON'),
    ('evening','EVENING'),
    ('dinner','DINNER'),
)

OCCASION_CHOICES = (
    ('anniversary','ANNIVERSARY'),
    ('birthday','BIRTHDAY'),
    ('get together','GET TOGETHER'),
    ('other','OTHER'),
)

class Reservation_Data(models.Model):
    Name = models.CharField(max_length = 20, default = "")
    Person = models.IntegerField(default = "")
    Mail = models.CharField(max_length = 50, default = "")
    Date = models.DateField(default = "")
    Time = models.TimeField(default = "")
    Phone = models.IntegerField(default = "")
    Plan = models.CharField(max_length = 10, choices = PLAN_CHOICES, default = "afternoon")
    Occasion = models.CharField(max_length = 20, choices = OCCASION_CHOICES ,default = "anniversary")
    Special = models.CharField(max_length = 200, default = "")


class Franchise_Data(models.Model):
    Name = models.CharField(max_length = 20, default = "")
    Phone = models.IntegerField(default = "")
    Mail = models.CharField(max_length = 50, default = "")
    City = models.CharField(max_length = 50, default = "")
    Investment = models.IntegerField(default = "")
    Information = models.CharField(max_length = 200, default = "")


class Contact_Data(models.Model):
    Name = models.CharField(max_length = 20, default = "")
    Mail = models.CharField(max_length = 50, default = "")
    Phone = models.IntegerField(default = "")
    Message = models.CharField(max_length = 200, default = "")