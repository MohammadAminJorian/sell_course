from django import forms
from .models import *

class courseee(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description' , ]
