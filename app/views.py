from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data ={
        "title": "Home",
        "name": "Welcome to Django",
        "course": "Django with React",
    }
    
    return render(request, "index.html",context=data)
def data_pass(request):
    data={
        "title": "Data",
        "name": "Django",
        "course": "Django with React",
    }

    return render(request,"datapass.html", context=data)

def contact(request):
    return render(request, "contact.html")

# Create your views here.
