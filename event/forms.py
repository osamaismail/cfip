from dataclasses import field
from django import forms
from .models import *
from captcha.fields import CaptchaField







class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class AttendForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields =  ('full_name','email','specialty','phoneNo','age','gender','governorates','education')