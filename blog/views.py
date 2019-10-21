from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .forms import CreatePostForm
from .models import Post


class IndexView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blog/index.html'


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
