from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


def index(request):
    post = Post.objects.all()
    return render(request, 'posts/index.html', context={'post': post})


class CreateViewClass(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'posts/create.html'
    success_url = '/'
