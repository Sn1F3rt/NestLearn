from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.TextField(max_length=100, default="student")

    def __str__(self):  # __unicode__ for Python 2
        # noinspection PyUnresolvedReferences
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # noinspection PyUnresolvedReferences
        Profile.objects.create(user=instance)

    instance.profile.save()
