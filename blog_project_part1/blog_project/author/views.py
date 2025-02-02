from django.shortcuts import render,redirect
from .forms import Author_form

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author = Author_form(request.POST)
        if author.is_valid():
            author.save()
            return redirect('add_author')
    else:
        author = Author_form()
    return render(request, 'add_author.html', {'form': author})
