from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm

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


class ProfileViewTest(TestCase):

    def test_redirects_to_login_if_not_authenticated(self):
        response = self.client.get(reverse('users:profile'))
        expected_url = reverse('users:login') + '?next=' \
                     + reverse('users:profile')
        self.assertRedirects(response, expected_url)

    def test_uses_profile_template(self):
        user = User.objects.create(username='test_user_name')
        self.client.force_login(user)
        response = self.client.get(reverse('users:profile'))
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_contains_authenticated_users_username(self):
        user = User.objects.create(username='test_user_name')
        self.client.force_login(user)
        response = self.client.get(reverse('users:profile'))
        self.assertContains(response, 'test_user_name')

    def test_passes_user_and_profile_forms_in_context(self):
        user = User.objects.create(username='test_user_name')
        self.client.force_login(user)
        response = self.client.get(reverse('users:profile'))
        self.assertIsInstance(response.context['u_form'], UserUpdateForm)
        self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)

    def test_updates_user_data_on_POST_if_form_valid(self):
        # TODO: Get form to validate with fake image.
        pass
