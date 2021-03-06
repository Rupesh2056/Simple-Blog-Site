from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def create_post(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_post(sender,instance,**kwargs):
    instance.profile.save()

