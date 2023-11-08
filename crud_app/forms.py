from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'description': forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Write a description'}),
            'title': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write a title'}),
            'important': forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }
        
    