from django.db import models
from cfipage.utils import validate_phone
import uuid
from django.contrib.auth.models import User




class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=100, blank=False, null=True)
    lname = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    phoneNo = models.CharField(max_length=11, blank=True, null=True, validators=[validate_phone], help_text='077 or 078 or 075')
    message = models.TextField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return (f'{self.fname} {self.lname}')


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100, blank=False, null=True)
    position = models.CharField(max_length=50, blank=False, null=True)
    about = models.CharField(max_length=150,blank=False, null=True)
    pic = models.ImageField(upload_to='team/', verbose_name='Event Image', blank=False, null=True)
    status = models.BooleanField(default=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkden = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.full_name
    