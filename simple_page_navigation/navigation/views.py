from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigation/About.html')

def contact(request):
    return render(request, 'navigation/Contact.html')