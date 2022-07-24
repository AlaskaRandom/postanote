from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import reverse_lazy #
from django.contrib.auth.mixins import (
    LoginRequiredMixin, # new
    UserPassesTestMixin) #

from django.contrib.auth.mixins import LoginRequiredMixin # new

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
class HomePageView(ListView): # new
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"

class BlogCreateView(LoginRequiredMixin,CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title','body']
    def form_valid(self, form): # new
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title','body']
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user



class COVID(ListView):
    model = Post
    template_name = 'covid.html'



