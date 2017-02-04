from django import forms
from .models import UserInfo,About

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ['username','email','password','reg','session','name','service','add','phn']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ['image_url','description']