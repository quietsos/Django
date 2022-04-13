from django.shortcuts import render

from .models import Event


def all_events(request):
     event_list = Event.objects.all()

     return render(request, 'event_list.html', {
          "event_list": event_list
     })


def home(request):
     return render(request,'home.html', {})




