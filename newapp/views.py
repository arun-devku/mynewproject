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
def assgnmnt4(request):
    return render (request, 'assgnmnt4.html')   
def assgnmnt5(request):
    return render (request, 'assgnmnt5.html')        
def assgnmnt6(request):
    return render (request, 'assgnmnt6.html')     
def assgnmnt7(request):
    return render (request, 'assgnmntbookmarks.html')    
def assgnmnt8(request):
    return render (request, 'assgnmnttable.html')     
def assgnmnt9(request):
    return render (request, 'table2.html') 
def assgnmnt10(request):
    return render (request, 'table3.html')
def assgnmnt11(request):
    return render (request, 'assgnmntcss1.html') 
def assgnmnt12(request):
    return render (request, 'assgnmntcss2.html') 
def assgnmnt13(request):
    return render (request, 'css3.html') 
def assgnmnt14(request):
    return render (request, 'css4.html')    
def assgnmnt15(request):
    return render (request, 'fbbootsrap.html')
def mypro(request):
    return render (request, 'myproject.html')            
def mypro2(request):
    return render (request, 'myproject2.html')   

 