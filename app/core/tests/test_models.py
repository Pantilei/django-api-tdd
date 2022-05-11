from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successeful(self):
        """
        Check if user is created with email
        """
        email = 'test@test.com'
        password = 'password123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normilized(self):
        """Test the email for a user normilized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="123455"
        )
        self.assertEqual(email.lower(), user.email)

    def test_new_user_valid_email(self):
        """Test creating new user raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="1234"
            )

    def test_create_super_user(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            email="test@gmail.com",
            password="12345s"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
