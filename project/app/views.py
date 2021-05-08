from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'app/home.html')

@login_required
def driver(request):
    drivers=Driver.objects.all()
    return render(request,'app/driver.html' , {'drivers':drivers})

@login_required
def vehicle(request):
    vehicles=Vehicle.objects.all()
    return render(request,'app/vehicle.html' , {'vehicles':vehicles})

@login_required
def bookinghistory(request):
    bookinghistorys=BookingHistory.objects.all()
    return render(request,'app/bookinghistory.html' , {'bookinghistorys':bookinghistorys})

@login_required
def bookingdetails(request):
    bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookingdetails.html' , {'bookingdetailss':bookingdetailss})

@login_required
def customeruser(request):
    customerusers=CustomerUser.objects.all()
    return render(request,'app/customeruser.html' , {'customerusers':customerusers})


def signupuser(request):
    if request.method=='GET':
        return render(request,'app/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')

            except IntegrityError:
                return render(request,'app/signupuser.html', {'form':UserCreationForm,'error':'user name has been taken'})
        else:
            return render(request,'app/signupuser.html', {'form':UserCreationForm,'error':'password did not match'})


def loginuser(request):
    if request.method=='GET':
        return render(request,'app/loginuser.html', {'form':AuthenticationForm()})
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'app/loginuser.html', {'form':AuthenticationForm(),'error':'username and password did not match'})
        else:
            login(request,user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')