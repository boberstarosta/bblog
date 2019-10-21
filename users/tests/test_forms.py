from django.contrib.auth import get_user_model
from django.test import TestCase

from users.forms import RegistrationForm

User = get_user_model()


class RegistrationFormTest(TestCase):

	def test_saves_new_user(self):
		form = RegistrationForm({
			'username': 'test_user',
			'password1': 'testpassword123',
			'password2': 'testpassword123',
		})
		new_user = form.save()
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(User.objects.first(), new_user)
