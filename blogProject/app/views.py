from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
# view of all posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'posts' 

# view of a single post (and its details)
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'