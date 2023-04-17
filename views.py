from django.shortcuts import render,redirect
from .models import toreview_mailus,guest
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import hotelregistration,signupform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html') 

def book_table(request):
    if request.method=="POST":
        a=request.POST['yourname']
        b=request.POST['youremail']
        c=request.POST['subject']
        d=request.POST['message']
        b1=toreview_mailus.objects.create(yourname=a,youremail=b,subject=c,message=d)
        b1.save()
        return HttpResponse("Your message has been sent. Thank you!")
     #else:
        #return render(request,'index.html')
        #return HttpResponse("Your message has been sent. Thank you!")

def get_mainpage(request):
    content={}
    content['data']=toreview_mailus.objects.all()
    return render (request,'dashboard1.html',content)  

def Delete(request,rid):
    x=toreview_mailus.objects.get(id=rid)
    x.delete()
    return  redirect('/main')   

def Edit(request,rid):
    if request.method=='POST':
        a=request.POST['yourname']
        b=request.POST['youremail']
        c=request.POST['subject']
        d=request.POST['message']
        b1=toreview_mailus.objects.filter(id=rid)
        b1.update(yourname=a,youremail=b,subject=c,message=d)
        return redirect('/')
    else:
        content={}
        content['data']=toreview_mailus.objects.get(id=rid)
        return render(request,'edit_review.html',content)    

class homepage(TemplateView):
    template_name="login.html"

def showform(request):
    if request.method=='POST':
        fm=hotelregistration(request.POST)
        #print(fm)
        if fm.is_valid():
            gname=fm.cleaned_data['name']
            gemail=fm.cleaned_data['email']
            #print(gname)
            #print(gemail)
            s1=guest.objects.create(name=gname,email=gemail)
            s1.save()
            return HttpResponse(gname+'-'+gemail)
    else:
        fm=hotelregistration()
    return render(request,'dform.html',{'form':fm})

def register(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        #print(fm)
        if fm.is_valid():
            #gname=fm.cleaned_data['username']
            #gpass=fm.cleaned_data['password1']
            #print(gname)
            #print(gpass)
            #u1=User(username=gname,password=gpass)
            #u1.save()
            #gname- jojo  gpass-jojo@1245
            #gname- kaka  gpass-kaka@1245
            fm.save()
            return redirect('/login')

    else:
        #fm=UserCreationForm()
        fm=signupform()
    return render (request,'signup.html',{'form':fm})  

def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            gname=fm.cleaned_data['username']
            gpass=fm.cleaned_data['password']
            #print(gname)
            #print(gpass)
            u=authenticate(username=gname,password=gpass)
            #print(u)
            if u is not None:
                login(request,u)
                #return HttpResponse("Profile")
                return redirect('/')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})

def user_profile(request):
    return render(request,'profile.html')

def user_logout(request):
    logout(request)
    return redirect('/login')