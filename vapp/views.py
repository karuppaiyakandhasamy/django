from django.shortcuts import render , redirect
from vapp.models import task ,adminpage
from vapp.forms import Userform , adminform
from django.contrib import messages
import urllib
from django.conf import settings
import json 
from django.http import JsonResponse
from django.http import HttpResponse  
# Create your views here.

def sample (request):
    
    return render (request,'vapp/index.html',)

def adminsample (request):
    
    return render (request,'vapp/admin.html',)



def register (request):
    
    form = Userform()
    user = task.objects.all()
    if request.method == 'POST':
        form = Userform(request.POST, request.FILES)
        form.save()
              

            
        return render (request,'vapp/index.html',{'form':form,})

    return render (request,'vapp/register.html',{'form':form,})

def login (request):
    form = Userform()
    user = task.objects.all ()

    if request.method == 'POST':
        try:
            userdetails = task.objects.get(Email=request.POST['Email'], Pwd = request.POST['Pwd'])
            print("username",userdetails)
            request.session['Email']=userdetails.Email
            request.session['Username'] = userdetails.Username
            request.session['Age'] = userdetails.id
            

            return render(request,'vapp/index.html',{'u':userdetails})
        except task.DoesNotExist as e:
            messages.success(request,"invalid")
    return render(request,'vapp/login.html' ,)

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'vapp/index.html')
    return render(request,'vapp/index.html')

def adminlogout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'vapp/sample.html')
    return render(request,'vapp/index.html')


def update (request,id):
    user = task.objects.get(id=id)
    form = Userform(instance=user)
    if request.method == "POST":
        form = Userform(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print("data updated")
            messages.success(request,"data updated")
    return render(request,'vapp/update.html' , {'form':form})


def adminupdate (request,id):
    user1 = adminpage.objects.get(id=id)
    form = adminform(instance=user1)
    if request.method == "POST":
        form = adminform(request.POST, request.FILES, instance=user1)
        if form.is_valid():
            form.save()
            print("data updated")
            messages.success(request,"data updated")
            
    return render(request,'vapp/adminupdate.html' , {'form':form})


def view (request,id):

    user = task.objects.get(id=id)

    return render (request,'vapp/show.html',{'task':user})


def adminview (request,id):

    user = adminpage.objects.get(id=id)

    return render (request,'vapp/adminshow.html',{'task':user})



def check (request):

    if request.method == "GET":
        un = request.GET['mm']
        print(un)
        
        check = task.objects.filter(Username=un)
        print(len(check))
    
        if len(check) == 0:
            print("hi")
            return HttpResponse("username valid")
        else:
            print("h")
            return HttpResponse(" plz change username ")

def checkemail (request):

    if request.method == "GET":
        data = request.GET['aemail']
        print(data)
        check = task.objects.filter(Email=data)
        if len(check) == 0:
            return HttpResponse("email valid")
        else:
            return HttpResponse("plz chznge emailaddres")

def checkphone (request):
    if request.method == "GET":
        idata = request.GET['iphone']
        checkphone = task.objects.filter(Phone=idata)

        if len(checkphone) == 0:
            return HttpResponse ("valid")
        else:
            return HttpResponse ("invalid")


def checkpwd (request):
    if request.method == "GET":
        idata = request.GET['iphone1']
        idata1 = request.GET['iphone2']
        print(idata)
        print(idata)
        

        if idata == idata1:
            return HttpResponse ("valid")
        else:
            return HttpResponse ("plz enter valid password ")

def checkform (request):
    if request.method == "GET":
        idata = request.GET['iphone1']
        idata1 = request.GET['iphone2']
        ipass = request.GET['ccp']
        ipass1 = request.GET['ccp1']
        checkemail = task.objects.filter(Email=idata)
        checkphone = task.objects.filter(Phone=idata1)
        print(idata)
        print(idata1)
        a = len(checkemail)
        ab = len(checkphone)
        print(a)
        print(ab)

        if a == 0 and ab == 0 and ipass == ipass1:
            print ("hii")
            return HttpResponse ("valid")
        

        else:
            print("h")
            return HttpResponse ("plz enter valid password ")


def adminlogin (request):
    
    user = adminpage.objects.all ()
    
    if request.method == 'POST':
        try:
            userdetails = adminpage.objects.get(Email=request.POST['Email'], Pwd = request.POST['Pwd'])
            print("username",userdetails)
            v = task.objects.all()
            request.session['Email']=userdetails.Email
            request.session['Username'] = userdetails.Username
            request.session['Age'] = userdetails.id
            

            return render(request,'vapp/admin.html',{'u':userdetails,'v':v})
        except task.DoesNotExist as e:
            messages.success(request,"invalid")
    return render(request,'vapp/adminlogin.html' ,)
