from django.db import models
import uuid
from tinymce import models as tinymce_models
from django.urls import reverse
from django.contrib.auth.models import User


BadgesList = (
    ('1','primary'),
    ('2','success'),
    ('3','info'),
    ('4','Warning'),
    ('5','danger'),
)



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True)
    badge = models.CharField(max_length=1, choices=BadgesList, null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    



class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, null=True)
    content = tinymce_models.HTMLField(null=True)
    mainPIC = models.ImageField(upload_to='news/', verbose_name='Main Image', null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'News'
    
    
    def __str__(self):
        return self.title
    
    def get_news_url(self):
        return reverse("news", kwargs={'id':self.id})
