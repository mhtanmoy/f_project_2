from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *

@login_required
def home(request):
    return render(request,'app/home.html')

@login_required
@manager_only
def driver(request):
    drivers=Driver.objects.all()
    return render(request,'app/driver.html' , {'drivers':drivers})

@login_required
@manager_only
def vehicle(request):
    vehicles=Vehicle.objects.all()
    return render(request,'app/vehicle.html' , {'vehicles':vehicles})

@login_required
@manager_only
def bookinghistory(request):
    bookinghistorys=BookingHistory.objects.all()
    return render(request,'app/bookinghistory.html' , {'bookinghistorys':bookinghistorys})

@login_required
@manager_only
def bookingdetails(request):
    bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookingdetails.html' , {'bookingdetailss':bookingdetailss})

@login_required
@manager_only
def customeruser(request):
    customerusers=CustomerUser.objects.all()
    return render(request,'app/customeruser.html' , {'customerusers':customerusers})

@unauthenticated_user
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

@unauthenticated_user
def signupuser(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
            
			admin = form.save()
			username = form.cleaned_data.get('username')

			Admin.objects.create(
				admin=admin,
				name=request.POST.get('name'),
                email=admin.email,
                contact_no=request.POST.get('contact_no'),
				)
			admin.save()
			login(request,admin)
			return redirect('home')			
	return render(request, 'app/signupuser.html',{'form':form} )

    