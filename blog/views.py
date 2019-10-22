from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Post

User = get_user_model()


class IndexView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blog/index.html'


class UserPostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView
):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Called by UserPassesTestMixin.
        Make sure only author can update the post."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView
):
    model = Post
    success_url = '/'

    def test_func(self):
        """Called by UserPassesTestMixin.
        Make sure only author can delete the post."""
        post = self.get_object()
        return self.request.user == post.author
