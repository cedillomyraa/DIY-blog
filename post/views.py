from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = 'post/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'post/new.html'
    model = Post
    fields = ['title','body']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = 'post/edit.html'
    model = Post
    fields = ['title','body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user