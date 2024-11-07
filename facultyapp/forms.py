from .models import AddCourse, marks
from django import forms

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']

class MarksForm(forms.ModelForm):
    class Meta:
        model = marks
        fields = ['student','course','marks']