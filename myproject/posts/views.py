from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required 
from . import forms

# Create your views here.
def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post (request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post': post})

@login_required(login_url='users:login')
def create_post(request):
    
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if (form.is_valid()):
            
            # save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()

            return redirect('posts:list')
    else:
        form = forms.CreatePost()

    return render(request, 'posts/form.html', {'form': form})