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


class PostDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.post = Post.objects.create(
            title='title', content='content', author=self.user
        )

    def test_http_status_code_is_success(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_uses_detail_template(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_title_and_content_present_in_response(self):
        post = Post.objects.create(
            title='Test Post Tile',
            content='Test post content.',
            author=self.user
        )
        response = self.client.get(post.get_absolute_url())
        self.assertContains(response, post.title)
        self.assertContains(response, post.content)


class CreatePostViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user')
        self.client.force_login(user)

    def test_renders_form_again_if_input_not_valid(self):
        response = self.client.post(reverse('blog:create_post'), data={
            'title': '',
            'content': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_creates_post_if_input_valid(self):
        response = self.client.post(reverse('blog:create_post'), data={
            'title': 'Test Post Title',
            'content': 'Test post content.'
        })
        self.assertEqual(Post.objects.first().title, 'Test Post Title')
        self.assertEqual(Post.objects.first().content, 'Test post content.')

    def test_redirects_to_detail_page_if_input_valid(self):
        response = self.client.post(reverse('blog:create_post'), data={
            'title': 'Test Post Title',
            'content': 'Test post content.'
        })
        post = Post.objects.first()
        self.assertRedirects(response, reverse('blog:detail', args=[post.pk]))

