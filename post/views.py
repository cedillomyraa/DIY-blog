from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = 'post/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'post/new.html'
    model = Post
    fields = ['title','author','body']

class PostUpdateView(CreateView):
    template_name = 'post/edit.html'
    model = Post
    fields = ['title','body']

class PostDetailView(DetailView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy('post_list')