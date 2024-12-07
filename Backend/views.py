from django.shortcuts import render

# Create your views here.


def indexpage(req):
    return render(req,"index.html")

def detailspage(req):
    return render(req,"adddetails.html")