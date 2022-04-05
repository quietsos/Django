from django.shortcuts import render

def home(request):
    name = "Sohan" 

    return render(request,'home.html', 
    {"name" : name})

