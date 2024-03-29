from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = '-some_datatime'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    queryset = Post.objects.filter(type__exact='NW').order_by('-some_datatime')
    template_name = 'flatpages/posts_search.html'
    context_object_name = 'posts_search'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

