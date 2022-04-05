from django.views import generic
from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 50

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(generic.CreateView):
    model = Post
    template_name = 'post.html'
    fields = '__all__'



