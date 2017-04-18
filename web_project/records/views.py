from django.shortcuts import render
from records.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



class PostListView(ListView):

    model = Post


class PostDetailView(DetailView):

    model = Post

class CreatePostView(CreateView):
	model = Post
	fields = ['title','slug','content', 'image']