import email
import string
from django.db import models
from django.forms import CharField


class  Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip code', max_length=10)
    phone = models.CharField("Contact phone", max_length=25)
    web = models.URLField("Website Address")
    email_address = models.EmailField("Email Address")

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField("user Email")

    def __str__(self):
        return self.first_name + " " + self.last_name



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, blank=True,null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser)

    def __str__(self):
        return self.name


    