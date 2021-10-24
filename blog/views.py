from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


