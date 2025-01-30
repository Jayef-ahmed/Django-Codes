from django import forms
from .models import StudentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name':'student Name',
            'roll': 'student Roll'
        }
        widgets ={
        }
        help_texts ={
            'name': "write your full name"
        }
        error_massages={
            'name':{'required': 'Your name is required'}
        }