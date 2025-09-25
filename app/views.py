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

    return render(request,"data_pass.html", context=data)

def MainPage(request):
    return render(request, "page.html")

# Create your views here.
