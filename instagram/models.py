from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/', blank = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)
    bio = models.TextField(max_length = 100)
    location = models.TextField(max_length = 60)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

class Post(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True)
    image_name = models.CharField(max_length = 30)
    image_caption = HTMLField(max_length = 200)
    profile = models.ForeignKey(User,on_delete = models.CASCADE, null = True)
    likes = models.IntegerField()
    photo_date = models.DateTimeField(auto_now_add=True, null = True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_all(cls):
       post = cls.objects.all()
       return post

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(profile, related_name='comments')
