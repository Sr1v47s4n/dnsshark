# dns_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Device,Rule

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ["device_name", "ip_address", "mac_address"]


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ["domain", "action"]
