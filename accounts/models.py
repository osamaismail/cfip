from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


LEVEL_LIST=(
    ('1','Administrator'),
    ('2','Manager'),
    ('3','Editor'),
    ('4','Data Entry')
    )


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, blank=True, null=False, choices=LEVEL_LIST, default=3)
    inactive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username
    
    def get_user_url(self):
        return reverse("edit", kwargs={'id':self.id})
    


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()