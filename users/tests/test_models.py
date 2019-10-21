from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class ProfileModelTest(TestCase):

    def test_default_image_url_is_media_default_jpg(self):
        user = User.objects.create(username='test_user')
        self.assertEqual(
            user.profile.image.url,
            settings.MEDIA_URL + 'default.jpg'
        )
