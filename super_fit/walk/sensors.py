from django.contrib.auth.models import User
from .models import Walk
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_walk(sender, instance, created, **kwargs):
    if created:
        Walk.objects.create(staff=instance, )

@receiver(post_save, sender=User)
def save_walk(sender, instance, **kwargs):
    instance.walk.save()