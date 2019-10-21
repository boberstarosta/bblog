from django.views import generic

from .models import Post


class IndexView(generic.ListView):
	model = Post
	paginate_by = 10
	context_object_name = 'posts'
	template_name = 'blog/index.html'
