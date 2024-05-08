from django.views import generic
from django.urls import reverse_lazy

from apps.posts.models import Post
from apps.posts.forms import PostForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('index')


class PostRetrieveView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'posts'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('index')


class PostDestroyView(generic.DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('index')