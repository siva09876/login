from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,StudentForm

class studentform(UserCreationForm):
    class Meta:
        model=MyUser
        
        fields= ['username','email','password1','password2']

class Student_Form(ModelForm):
    class Meta:
        model=StudentForm
        widgets={'gender':forms.RadioSelect,'dob':forms.TextInput(attrs={'placeholder':'DD/MM/YYYY'})}
        fields='__all__'
        exclude=['user']