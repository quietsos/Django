from distutils.command.build_scripts import first_line_re
import email
from django.db import models
from django.forms import CharField




class Venue(models.Model):
    name = models.CharField("Venu name", max_length=50)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    web = models.URLField("website urls")
    email_address = models.EmailField("Email Address")


    def __str__(self):
        return self.name



class Users(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email=models.EmailField("user email")


    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, blank=True,null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Users)

    def __str__(self):
        return self.name  




