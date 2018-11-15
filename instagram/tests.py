from django.test import TestCase
from .models import Post,profile

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =profile(profile_photo="image.jpeg",bio="food for good life")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()


class PostTestClass(TestCase):


    def setUp(self):
        self.new_image=Post(image="image.jpg",image_name="joe",image_caption="color image",photo_date="two minutes ago")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Post))

    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.new_image.save_post()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    # def test_delete_method(self):
    #     '''
    #     Function that tests whether an image can be deleted from the database
    #     '''
    #     self.new_image.save_post()
    #     self.new_image.delete_post()
