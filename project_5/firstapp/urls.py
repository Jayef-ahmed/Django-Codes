
from django.urls import path
from .views import index,about,submit_form,DjangoForm,StudentForm,Password_Validation

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('form/', submit_form, name='submitform'),
    path('django_form/', Password_Validation, name='django_form'),
]
