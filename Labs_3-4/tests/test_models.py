from django.test import TestCase
from e_commerse_auction.models import User, Listing, Bid, Comment
from django.utils import timezone


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='udav', first_name='Max', last_name='Chmurov')

    def test_user_model_entry(self):
        """
        Test User model data insertion/types/field attributes
        """
        test_user = self.user
        self.assertTrue(isinstance(test_user, User))

    def test_user_str(self):
        """
        Test User __str__ conversion
        """
        test_user = self.user
        self.assertEquals(test_user.__str__(), 'udav (Max Chmurov)' )


class ListingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='python', first_name='Vitaly', last_name='Butoma')
        self.listing = Listing.objects.create(user=self.user, title='Learning Python', price='20.0',
                        description='Import this', date=timezone.now(), photo='https://files.realpython.com/media/django-pony.c61d43c33ab3.png',
                        category='Education', status='True')

    def test_listing_model_entry(self):
        """
        Test Listing model data insertion/types/field attributes
        """
        test_listing = self.listing
        self.assertTrue(isinstance(test_listing, Listing))

    def test_listing_str(self):
        """
        Test Listing __str__ conversion
        """
        test_listing = self.listing
        self.assertEquals(test_listing.__str__(), f'User:{test_listing.user} Item:{test_listing.title} Price:{test_listing.price} Date Listed:{test_listing.date}')

    def test_title_max_length(self):
        """
        Test title max_length limit
        """
        test_listing = self.listing
        max_length = test_listing._meta.get_field('title').max_length
        self.assertEquals(max_length, 64)

    def test_photo_url_max_length(self):
        """
        Test photo url max_length limit
        """
        test_listing = self.listing
        max_length = test_listing._meta.get_field('photo').max_length
        self.assertEquals(max_length, 200)

    def test_description_max_length(self):
        """
        Test description max_length limit
        """
        test_listing = self.listing
        max_length = test_listing._meta.get_field('description').max_length
        self.assertEquals(max_length, 256)


class BidModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kavalski', first_name='Vladiskav', last_name='Kovalev')
        self.listing = Listing.objects.create(user=self.user, title='Learning Python', price='20.0',
                        description='Import this', date=timezone.now(), photo='https://files.realpython.com/media/django-pony.c61d43c33ab3.png',
                        category='Education', status='True')
        self.bid = Bid.objects.create(listing=self.listing, price='100.0', bidder=self.user)

    def test_bid_model_entry(self):
        """
        Test Bid model data insertion/types/field attributes
        """
        test_bid = self.bid
        self.assertTrue(isinstance(test_bid, Bid))

    def test_bid_model_str(self):
        """
        Test Bid __str__ conversion
        """
        test_bid = self.bid
        self.assertEquals(test_bid.__str__(), f'Listing:{test_bid.listing} price:{test_bid.price}')


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='chort', first_name='Alex', last_name='Letoho')
        self.listing = Listing.objects.create(user=self.user, title='Learning Python', price='20.0',
                        description='Import this', date=timezone.now(), photo='https://files.realpython.com/media/django-pony.c61d43c33ab3.png',
                        category='Education', status='True')
        self.comment = Comment.objects.create(user=self.user, date=timezone.now(), comment='Go strikeball', listing=self.listing)

    def test_comment_model_entry(self):
        """
        Test Comment model data insertion/types/field attributes
        """
        test_comment = self.comment
        self.assertTrue(isinstance(test_comment, Comment))

    def test_comment_str(self):
        """
        Test Comment __str__ conversion
        """
        test_comment = self.comment
        self.assertEquals(test_comment.__str__(), f'Date:{test_comment.date} Comment:{test_comment.comment} Listing:{test_comment.listing}')

    def test_comment_max_length(self):
        """
        Test Comment max_length
        """
        test_comment = self.comment
        max_length = test_comment._meta.get_field('comment').max_length
        self.assertEquals(max_length, 256)
