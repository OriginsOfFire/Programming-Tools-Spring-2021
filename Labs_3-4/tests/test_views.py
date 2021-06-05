from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

from e_commerse_auction.models import Listing
from e_commerse_auction.views import *


class IndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test', email='test@mail.ru')
        self.user.save()

    #самописный User перекрывает встроенного
    def test(self):
        resp = self.client.post('/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(resp.status_code, 200)

    def test_login_view_page(self):
        resp = self.client.get('/login/')
        self.assertContains(resp.content, 'username')


class ListingViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='python', first_name='Vitaly', last_name='Butoma')
        self.listing = Listing.objects.create(user=self.user, title='Learning Python', price='20.0',
                        description='Import this', date=timezone.now(), photo='https://files.realpython.com/media/django-pony.c61d43c33ab3.png',
                        category='Education', status='True')

    def test(self):
        resp = self.client.get('/listing/1')
        self.assertEqual(resp.status_code, 200)
