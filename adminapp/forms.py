from django import forms
from .models import Task, StudentList, feedback, Manager

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file')


class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email', 'phone_number', 'textfield']

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'email', 'phone_number', 'address']

