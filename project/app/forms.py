from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import ModelChoiceField


class CreateUserForm(UserCreationForm):
	name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_no = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ['name', 'username','contact_no' , 'email', 'password1', 'password2']

class AdminForm(ModelForm):
	class Meta:
		model = Admin
		fields = '__all__'
		exclude = ['admin']

class DriverFrom(ModelForm):
	insurance_type = ModelChoiceField(queryset=Insurance.objects.all())
	class Meta:
		model = Driver
		fields = '__all__'
		exclude = ['driver_id']

class CustomerUserFrom(ModelForm):
	class Meta:
		model = CustomerUser
		fields = '__all__'
		exclude = ['User_Id']


class VehicleFrom(ModelForm):
	brand = ModelChoiceField(queryset=Brand.objects.all())
	model = ModelChoiceField(queryset=BrandModel.objects.all())
	class Meta:
		model = Vehicle
		fields = ['brand','model','fare_per_km' ,'air_conditioned','luggage_capacity','number_of_seat','front_image','side_image','back_image']



class NotificationFrom(ModelForm):
	
	class Meta:
		model = Notification
		fields = '__all__'


class CouponsFrom(ModelForm):
	class Meta:
		model = Coupons
		fields = '__all__'


class AssignDriverForm(ModelForm):
	class Meta:
		model =BookingDetails
		fields = ['assign_driver']

class BrandFrom(ModelForm):
	class Meta:
		model = Brand
		fields = ['brand_name']

class InsuranceFrom(ModelForm):
	class Meta:
		model = Insurance
		fields = ['insurance_type']

class BrandModelFrom(ModelForm):
	class Meta:
		model = BrandModel
		fields = '__all__'
