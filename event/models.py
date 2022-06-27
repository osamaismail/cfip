from distutils.command.upload import upload
from operator import mod
from django.db import models
import uuid
from tinymce import models as tinymce_models
from django.urls import reverse
from django.contrib.auth.models import User
from cfipage.utils import validate_phone




class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, blank=False, null=True)
    content = tinymce_models.HTMLField(blank=False, null=True)
    eventPIC = models.ImageField(upload_to='events/', verbose_name='Event Image', blank=True)
    eventDate = models.DateField(null=True)
    eventTime = models.TimeField(null=True)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    def get_event_url(self):
        return reverse("event", kwargs={'id':self.id})
    



GENDER_LIST=(
    ('M','Male'),
    ('F','Female')
    )

GOVERNORATES_LIST=(
    ('AN','الانبار'),
    ('BB','بابل'),
    ('BG','بغداد'),
    ('BA','البصرة'),
    ('DQ','ذي قار'),
    ('QA','القادسية'),
    ('DI','ديالى'),
    ('DA','دهوك'),
    ('AR','اربيل'),
    ('KA','كربلاء'),
    ('KI','كركوك'),
    ('MA','ميسان'),
    ('MU','مثنى'),
    ('NA','النجف'),
    ('NI','نينوى'),
    ('SD','صلاح الدين'),
    ('SU','السليمانية'),
    ('WA','واسط')
    )

SPECIALTY_LIST=(('MD','طبية'),
                ('ENG','هندسية'),
                ('SCI','العلوم'),
                ('FE','كلية التربية'),
                ('IN','معهد'),
                ('S','طالب اعدادية'),
                ('OTH','اخرى')
                )


EDUCATION_LIST=(
                ('IS','متوسطة'),
                ('HS','اعدادية'),
                ('DIP','دبلوم'),
                ('BAC','بكلوريوس'),
                ('MD','ماجستير'),
                ('DOC','دكتوراه'),
                ('OTH','اخرى'),
                )


AGE_LIST= tuple((str(age),str(age)) for age in range(14,90))



class Attend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False, null=True)
    full_name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    specialty = models.CharField(max_length=3, choices=SPECIALTY_LIST, blank=False, null=True)
    education = models.CharField(max_length=3, choices=EDUCATION_LIST, blank=False, null=True)
    phoneNo = models.CharField(max_length=11, blank=True, null=True, validators=[validate_phone], help_text='077 or 078 or 075')
    age = models.CharField(max_length=2, choices=AGE_LIST, blank=False, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=True)
    governorates=models.CharField(max_length=2, choices=GOVERNORATES_LIST, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    
    
    def __str__(self):
        return self.event.title
    
   
