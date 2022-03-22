from urllib import response
from django.test import TestCase


class URLTests(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration_page(self):
        response = self.client.get('/user_register/')
        self.assertEqual(response.status_code, 200)