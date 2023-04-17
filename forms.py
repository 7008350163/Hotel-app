from django import forms
from .models import guest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class hotelregistration(forms.ModelForm):
    class Meta:
        model=guest  
        fields=['name','email']  

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']        