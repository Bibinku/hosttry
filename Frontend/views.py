from django.shortcuts import render,redirect
from Backend.models import DetailsDB



# Create your views here.

def homepage(req):
    data = DetailsDB.objects.all()
    return render(req, "home.html",{'data':data})

def roomspage(req,Aid):
    data = DetailsDB.objects.all()
    cata = DetailsDB.objects.get(id=Aid)
    return render(req,"Rooms.html",{'data':data,'cata':cata})
