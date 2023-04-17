forms.py--->
from django import forms
from .models import guest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class hotelregistration(forms.ModelForm):
    class Meta:
        model=guest  
        fields=['name','email']  
from django.db import models

