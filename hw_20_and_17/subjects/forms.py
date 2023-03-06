from django.forms import ModelForm
from .models import Subject
from django import forms

class Subject_create_form(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Название предмета'
            })
        }