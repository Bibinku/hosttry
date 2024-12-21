from django.shortcuts import render,redirect
from Backend.models import DetailsDB
from Frontend.models import ContactDB
from django.contrib import messages



# Create your views here.

def homepage(req):
    data = DetailsDB.objects.all()
    return render(req, "home.html",{'data':data})

def roomspage(req,):
    data = DetailsDB.objects.all()

    return render(req,"Rooms.html",{'data':data})

def contactpage(req):
    return render(req,"contact.html")

def aboutpage(req):
    return render(req,"aboutpage.html")



def savecontact(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('number')
        obj = ContactDB(name=a, email=b, number=c,)
        obj.save()
        messages.success(req, "Thanks for Contacting Us ")


        return redirect(homepage)

def savehomecontact(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('number')
        obj = ContactDB(name=a, email=b, number=c,)
        obj.save()
        messages.success(req, "Thanks for Contacting Us ")


        return redirect(homepage)

def singleroom(req,Rid):
    data = DetailsDB.objects.all()
    cata = DetailsDB.objects.get(id=Rid)
    return render(req,"singleroom.html",{'data':data,'cata':cata})

def ourservices(req):
    return render(req,"ourservices.html")
