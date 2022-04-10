from django.test import TestCase
from .models import Profile,Project,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTEst(TestCase):
    def setUp(self):
        '''
        Set up class to create a new profile
        '''
        self.toni = User(username = 'toni',email = 'toni@gmail.com')
        self.toni = Profile(user = self.toni,user_id = 1,bio = 'Web design',profilepic = 'picture.jpg',info = 'more')

    def test_instance(self):
        '''
        Test class to test instantiation
        '''
        self.assertTrue(isinstance(self.toni,Profile))

    def test_save_profile(self):
        '''
        Test to test if a profile is saved
        '''
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        '''
        Test to see if a profile can be deleted 
        '''
        self.toni.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)