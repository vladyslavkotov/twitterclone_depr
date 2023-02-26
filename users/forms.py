from django.contrib.auth.forms import *
from django.forms import ModelForm

from .models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")



