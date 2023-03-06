from django.forms import ModelForm
from .models import Student, Group
from django import forms


class Group_Create_Form(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Название группы'
            })
        }

class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Фамилия'
            }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Телефон'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'image': forms.FileInput(attrs={'class': 'img-fluid'}),
            'group': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'}),
            'on_subject': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
        }    