from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models import Profile

class register_form(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class user_edit_form(forms.ModelForm):
    email = forms.EmailField(required=False)
    firstname=forms.CharField(max_length=20, required=False)


    class Meta:
        model=User
        fields=['username','email']

class profile_edit_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic']



