from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *



def home(request):
    return HttpResponse('hello')

def arundev(request):
    if request.method=="POST":
        try:

            username=request.POST["email"]
            password=request.POST["password"]
            logobj=Logindetails.objects.get(username=username,password=password)
            request.session['logid']=logobj.id
            request.session['usenme']=logobj.username
            return render (request, 'fbhome.html')  
        except:
            return render(request, 'facebook.html',{'msg':'invalid password or username'})


              
    else:
        return render (request, 'facebook.html') 
        

    

def fbprofile(request):
   
    if request.method== 'POST':
        print("post working")
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        mobilenumber=request.POST["contact_number"]
        logid= request.session['logid']
        userdetails=Details.objects.get(user=logid)
        print(userdetails.firstname)
        userdetails.firstname=firstname
        print(userdetails.firstname)
        userdetails.lastname=lastname
        userdetails.phonenumber=mobilenumber
        userdetails.save()
        profile=""
        if 'profile' in request.FILES:
            profile=request.FILES['profile']    
            logobj=Logindetails.objects.get(id=logid)
            print(logobj)
            check=propic.objects.filter(user=logid).first()
            print(check)
        
            if check:
                check.propicture=profile
                check.save()
                profilepic=check.propicture
            else:

                propicobj=propic(propicture=profile,user=logobj)
                propicobj.save()
                profilepic=propicobj.propicture
            return render(request, 'fbhomebase.html',{'userdetails':userdetails,"profile":profilepic})    
        else:

            return redirect("/newapp/fbprofile")
       
       
    else:
        
        logindata=request.session['logid']
        userdetails=Details.objects.get(user=logindata)
        print(UserDetais)
        try:
            profile=propic.objects.get(user=logindata)
            return render(request, 'fbhomebase.html',{'userdetails':userdetails,"profile":profile.propicture})    

        except:
            return render(request, 'fbhomebase.html',{'userdetails':userdetails,"profile":""})    

        



 



def firstassgnmnt(request):
    user=UserDetais.objects.all()
    print(user)
    # username='arun'
    # age=24
    return render (request, 'firstassgnmt.html',{'user':user})  
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
def fbbase(request):
    return render (request, 'basaefb.html')  
def fblog1(request):
    return render (request, 'fblogincrct.html')
def fblog2(request):
    return render (request, 'fbincrctemail.html')
def fblog3(request):
    return render (request, 'fbhome.html')
def mypro1(request):
    return render (request, 'myproject1.html') 
def new2(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contactnumber=request.POST['contactnumber']
        dateofbirth=request.POST['dateofbirth']
        data=Student(firstname=firstname,lastname=lastname,contactnumber=contactnumber,dateofbirth=dateofbirth)
        data.save()

    return render (request, 'student.html') 

# def new1(request):
#     if request.method=="POST": 
#         firstname=request.POST.get('firstname')
#         lastname=request.POST.get('lasttName')
#         password=request.POST.get('password')
#         mobilenumber=request.POST.get('mobilenumber')
#         emailid=request.POST.get('email')

#         userobj=UserDetais(username=emailid,password=password,firstname=firstname,lastname=lastname,phonenumber=mobilenumber)
#         userobj.save()

#         print(firstname)
#         return render (request, 'new21.html')  
#     else:
#         print("inside get")
#         return render (request, 'new21.html')       
                 

def new1(request):
    if request.method=="POST": 
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lasttName')
        password=request.POST.get('password')
        mobilenumber=request.POST.get('mobilenumber')
        emailid=request.POST.get('email')
        logobj=Logindetails(username=emailid,password=password)
        logobj.save()
        userobj=Details(firstname=firstname,lastname=lastname,phonenumber=mobilenumber,user=logobj)
        userobj.save()

        print(firstname)
        return render (request, 'new21.html')  
    else:
        print("inside get")
        return render (request, 'new21.html') 


def json(request):
    data=Details.objects.values()
    print(data)
    userdata=list(data)
    print(userdata)
    
    return JsonResponse({'data':userdata})
def checkusername(request):
    username=request.GET['user']
    print(username)
    check=Logindetails.objects.filter(username=username).exists()
    print(check)
    if check:
        return JsonResponse({"check":'exist'})
    else:
        return JsonResponse({"check":"not exist"})
    
                 


 