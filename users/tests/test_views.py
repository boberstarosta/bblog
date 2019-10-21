from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.forms import RegistrationForm

User = get_user_model()


class RegisterViewTest(TestCase):

    def test_uses_register_template(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_passes_registration_form_in_context(self):
        response = self.client.get(reverse('users:register'))
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_renders_form_again_if_input_not_valid(self):
        response = self.client.post(reverse('users:register'), data={
            'username': '123456789',
            'password1': 'testpassword',
            'password2': 'wrong-password-confirmation'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_creates_user_if_input_valid(self):
        response = self.client.post(reverse('users:register'), data={
            'username': 'test_user',
            'password1': 'testpassword1234',
            'password2': 'testpassword1234'
        })
        self.assertEqual(User.objects.first().username, 'test_user')

    def test_redirects_to_login_page_if_input_valid(self):
        response = self.client.post(reverse('users:register'), data={
            'username': 'test_user',
            'password1': 'testpassword1234',
            'password2': 'testpassword1234'
        })
        self.assertRedirects(response, reverse('users:login'))
