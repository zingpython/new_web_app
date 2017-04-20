from django.shortcuts import render
from records.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



class PostListView(ListView):

    model = Post


class PostDetailView(DetailView):

    model = Post

class CreatePostView(CreateView):
	model = Post
	fields = ['title','slug','content', 'image']


class UpdatePostView(UpdateView):
	model = Post
	fields =['title', 'slug','content', 'image']
	template_name_suffix = '_update_form'



class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('records:list_posts')
















