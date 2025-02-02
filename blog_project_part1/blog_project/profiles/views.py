from django.shortcuts import render,redirect
from .forms import profile_form

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile = profile_form(request.POST)
        if profile.is_valid():
            profile.save()
            return redirect('add_profile')
    else:
        profile = profile_form()
    return render(request, 'add_profile.html', {'form': profile})