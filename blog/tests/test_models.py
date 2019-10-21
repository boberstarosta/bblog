from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from blog.models import Post

User = get_user_model()


class PostModelTest(TestCase):

    def test_title_required(self):
        user = User.objects.create(username='test_user')
        post = Post(content='post content', author=user)
        with self.assertRaises(ValidationError):
            post.save()
            post.full_clean()

    def test_content_required(self):
        user = User.objects.create(username='test_user')
        post = Post(title='post title', author=user)
        with self.assertRaises(ValidationError):
            post.save()
            post.full_clean()

    def test_author_required(self):
        post = Post(title='post title', content='post content')
        with self.assertRaises(IntegrityError):
            post.save()
            post.full_clean()

    def test_str_returns_title(self):
        user = User.objects.create(username='test_user')
        post = Post(title='post title', content='post content', author=user)
        self.assertEqual(str(post), post.title)
