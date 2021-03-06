from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com",
            password="123dd"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="1234d",
            name="User name"
        )

    def test_users_listed(self):
        """Test that users are listed in user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_change_page(self):
        """Test user change page exists"""
        url = reverse("admin:core_user_change", args=[
                      self.user.id])  # /admin/core/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        """Test user add page exists"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
