from django.urls import path,include
from . import views

urlpatterns = [

    # int : numbers
    # str : stings
    # path : whole urls /
    # slug : hyphen-and_uderscroes_stuff 
    # UUID: universally unique identifier


    path('', views.calender, name="calender"),
    path('<int:year>/<str:month>/', views.calender, name="calender")
]
