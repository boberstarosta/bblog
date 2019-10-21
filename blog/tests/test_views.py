from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post

User = get_user_model()


class IndexViewTest(TestCase):

    def test_http_status_code_is_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uses_index_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_passes_ten_newest_posts_in_context(self):
        user = User.objects.create(username='test_user')
        posts = [
            Post.objects.create(
                title=f'post {i}', content='content', author=user)
            for i in range(20)
        ]
        response = self.client.get('/')
        self.assertEqual(
            list(response.context['posts']),
            posts[:-11:-1]
        )
