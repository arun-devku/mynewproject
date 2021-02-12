from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('hello')

def arundev(request):
    return render (request, 'facebook.html')  
def firstassgnmnt(request):
    return render (request, 'firstassgnmt.html')  
def assgnmnt2(request):
    return render(request, 'assgnmnt2.html')   
def assgnmnt3(request):
    return render (request, 'assgnmnt3.html') 
def bootstrap(request):
    return render(request, 'bootstrap.html')           


 