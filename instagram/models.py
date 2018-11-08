from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

# Create your models here.
class profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/', blank = True)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)
    bio = models.TextField(max_length = 100)

    def save_profile(self):
        save.self()

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
    profile = models.ForeignKey(,on_delete = models.CASCADE, null = True)
    likes = models.IntegerField()
    comment = models.TextField(max_length = 200)
    photo_date = models.DateTimeField(auto_now_add=True, null = True)
