from django import forms
from django.forms import ModelForm
from vapp.models import task ,adminpage

class Userform (forms.ModelForm):
    
    class Meta:
        model = task
        fields = "__all__"


class adminform (forms.ModelForm):
    
    class Meta:
        model = adminpage
        fields = "__all__"
