from django import forms
from .models import Author

class Author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # Field = ['name', 'bio']
        # exclude = ['bia']