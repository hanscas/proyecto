from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class HomeBlogListView(ListView):
    model = Post
    template_name = 'home.html'

class HomeBlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class HomeBlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['titulo', 'autor', 'cuerpo']
    success_url = reverse_lazy('home')

class HomeBlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['titulo', 'autor', 'cuerpo']
    success_url = reverse_lazy('home')

class HomeBlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')