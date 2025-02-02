from django.shortcuts import render,redirect
from .forms import Add_Post
from .models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post = Add_Post(request.POST)
        if post.is_valid():
            post.save()
            return redirect("add_post")
    else:
        post = Add_Post()
    return render(request, 'add_post.html', {'form': post})

def edit_post(request, id):
    posts = Post.objects.get(pk=id)
    post = Add_Post(instance=posts)
    if request.method == 'POST':
        post = Add_Post(request.POST,instance=posts)
        if post.is_valid():
            post.save()
            return redirect("homepage")
    return render(request, 'add_post.html', {'form': post})

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("homepage")