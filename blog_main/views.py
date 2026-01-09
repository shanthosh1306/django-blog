
print("views.py is loaded")
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("home view is called")
    #return HttpResponse('<h2>Homepage</h2>')
    return render(request,'home.html')