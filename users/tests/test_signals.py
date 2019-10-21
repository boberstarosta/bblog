from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import Profile

User = get_user_model()


class UserSignalsTest(TestCase):

    def test_profile_created_when_user_created(self):
        user = User.objects.create(username='test_user')
        self.assertEqual(Profile.objects.first().user.username, 'test_user')

    def test_profile_saved_when_user_saved(self):
        user = User.objects.create(username='test_user')
        user.profile.image = 'test.jpg'
        user.save()
        self.assertEqual(Profile.objects.first().image, 'test.jpg')
