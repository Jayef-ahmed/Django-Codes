from django.shortcuts import render,redirect
from .forms import Add_Category

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category = Add_Category(request.POST)
        if category.is_valid():
            category.save()
            return redirect("add_category")
    else:
        category = Add_Category()
    return render(request, 'add_category.html', {'form': category})