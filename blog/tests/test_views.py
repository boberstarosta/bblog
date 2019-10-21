from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_http_status_code_is_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uses_index_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertTemplateUsed(response, 'blog/index.html')
