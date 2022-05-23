from email.policy import default
from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="my_profile")
    about = models.TextField()
    image = ResizedImageField(size = [320,280],upload_to = "profile_images", default = f"{settings.BASE_DIR}/media/profile_images/profile-avatar.svg", force_format = "jpeg", quality = 100)

    def __str__(self):
        return self.user.username + " profile"


class Subscribers(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name = "my_subscribers")
    subscribed = models.ManyToManyField(User, related_name ="subscribed")

    def __str__(self):
        return self.user.username + " subscribers"
    
    def is_a_subscriber(self,user):
        user = User.objects.get(id = user.id)
        if user in self.subscribed.all():
            return True
        return False