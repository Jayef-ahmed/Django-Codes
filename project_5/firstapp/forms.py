from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label ="Full Name: ", help_text="total lenght must be 70 charecters", required=False, widget = forms.Textarea(attrs={'id' : 'text-area', 'class':'class1 class2', 'placeholder' : 'Enter Your Full Name'}))
    email = forms.EmailField(label ="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget = forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'Date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "datetime-local"}))
    CHOICE = [('S', 'Small'),('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    MEAL = [('P', 'Peparoni'), ('M', 'Masroom'), ('C', 'chess')]
    pizza = forms.MultipleChoiceField(choices=MEAL ,widget=forms.CheckboxSelectMultiple)

# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Your email must be contain .com')
#     #     return valemail
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name with at least 10 charecter')
#         if '.com' not in valemail:
#             raise forms.ValidationError('Your email must be contain .com')

def check_len(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 charecters")
class studentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 charecter')])
    text = forms.CharField(widget=forms.TextInput,validators=[check_len])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a Valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='age must be maximum 34'), validators.MinValueValidator(21, message='age must be at least 21')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='file must be pdf format')])


class PasswordValidation(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['Confirm_password']
        valname = self.cleaned_data['name']
        if pass1 != pass2:
            raise forms.ValidationError('pass does not match')
        if len(valname) < 10:
            raise forms.ValidationError('Name must be at least 10 charecters')