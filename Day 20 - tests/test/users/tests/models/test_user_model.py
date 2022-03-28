from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(
            name='sara',
            last_name='kaner',
            user_name='terminator',
            email='sara@gmail.com',
            address='usa, new york',
            remmeber_me=True,
            password='123456',
        )
    
    def test_name(self):
        user = User.objects.get(id=1)
