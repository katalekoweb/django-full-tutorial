from django.shortcuts import render
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
    form = forms.CreatePost()
    return render(request, 'posts/form.html', {'form': form})