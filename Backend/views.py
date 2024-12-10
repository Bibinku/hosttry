from django.shortcuts import render, redirect
from Backend.models import DetailsDB
from Frontend.models import ContactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

# Crete a function called indexpage

def indexpage(req):
    return render(req, "index.html")


# create a details function
def detailspage(req):
    return render(req, "adddetails.html")


# To save details
def savedetails(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('description')
        c = req.POST.get('price')
        d = req.POST.get('advprice')

        img1 = req.FILES['roomimage1']
        img2 = req.FILES['roomimage2']
        img3 = req.FILES['roomimage3']
        obj = DetailsDB(name=a, description=b, price=c, advprice=d, roomimage1=img1, roomimage2=img2, roomimage3=img3)
        obj.save()
        messages.success(req, "Details Add Successfully")

        return redirect(displaydetails)


# to display details
def displaydetails(req):
    data = DetailsDB.objects.all()
    return render(req, "displaydetails.html", {'data': data})


# function used to edit the details
def editdetails(req, Did):
    data = DetailsDB.objects.get(id=Did)
    return render(req, "editdetails.html", {'data': data})


def updatedetails(req, Uid):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('description')
        c = req.POST.get('price')
        d = req.POST.get('advprice')

        try:
            img1 = req.FILES['roomimage1']
            img2 = req.FILES['roomimage2']
            img3 = req.FILES['roomimage3']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)
            file2 = fs.save(img2.name, img2)
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file1 = DetailsDB.objects.get(id=Uid).roomimage1
            file2 = DetailsDB.objects.get(id=Uid).roomimage2
            file3 = DetailsDB.objects.get(id=Uid).roomimage3

    DetailsDB.objects.filter(id=Uid).update(name=a, description=b, price=c, advprice=d, roomimage1=file1,
                                            roomimage2=file2, roomimage3=file3)
    messages.success(req, "Details Updated Successfully")

    return redirect(displaydetails)


def deletedetails(req, Delid):
    data = DetailsDB.objects.filter(id=Delid)
    data.delete()
    messages.warning(req, "Details Deleted Successfully")
    return redirect(displaydetails)


def adminlogin(req):
    return render(req, "adminlogin.html")


def admin(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request, x)
                request.session['username'] = a
                request.session['password'] = b
                messages.success(request, "Welcome..")
                return redirect(indexpage)
            else:
                messages.warning(request, "Invaild username or password")
                return redirect(adminlogin)
        else:
            messages.warning(request, "Please check before enter ")
            return redirect(adminlogin)


def adminlogout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req, "Logout Successfully")
    return redirect(adminlogin)

def displaycontact(req):
    cata = ContactDB.objects.all()
    return render(req, "displaycontact.html", {'cata': cata})

def deletecontact(req, Cid):
    cata = ContactDB.objects.filter(id=Cid)
    cata.delete()
    messages.warning(req, "Details Deleted Successfully")
    return redirect(displaycontact)