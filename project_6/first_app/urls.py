from django.urls import path
from .views import home,delete_student

urlpatterns = [
    path('', home, name="home_page"),
    path('delete/<int:roll>', delete_student, name='delete_student'),
]
