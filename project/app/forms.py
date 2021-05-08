from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Admin


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

