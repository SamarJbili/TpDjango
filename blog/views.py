from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' 
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postdetail.html'  
  
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'     
    fields = ['title', 'slug', 'content', 'status', 'image']  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')
    
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'slug', 'content', 'status', 'image']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/confirmdelete.html'  