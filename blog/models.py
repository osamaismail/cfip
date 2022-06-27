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

CATEGORIES_LIST = (
    ('1','OS'),
    ('2','Mobile Application'),
    ('3','GPU & CPU'),
)



class BlogCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, choices=CATEGORIES_LIST, null=True)
    badge = models.CharField(max_length=1, choices=BadgesList, null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    



class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, null=True)
    content = tinymce_models.HTMLField(null=True)
    mainPIC = models.ImageField(upload_to='blog/', verbose_name='Main Image', null=True)
    # category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_blog_url(self):
        return reverse("blog", kwargs={'id':self.id})
