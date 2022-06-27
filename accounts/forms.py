from dataclasses import field
from operator import mod
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from event.models import Event
from blog.models import Blog, BlogCategory
from news.models import News
from main.models import *





class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
        
        def save(self, commit=True):
            user = super(UserRegisterForm,self).save(commit=False)
            user.username= self.cleaned_data['username']
            user.first_name= self.cleaned_data['first_name']
            user.last_name= self.cleaned_data['last_name']
            user.email= self.cleaned_data['email']
            if commit:
                user.save()
            return user
    
    

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['level','inactive']


class EventsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','content','eventPIC','eventDate','eventTime','facebook','twitter')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','mainPIC','source')


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','mainPIC','source','accepted','deleted')
        

class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ('name',)     


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','content','mainPIC','source','facebook','twitter')


class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','content','mainPIC','source','facebook','twitter','accepted','deleted')   


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('full_name','position','pic','about','facebook','twitter','linkden')

class EditTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('full_name','position','pic','about','facebook','twitter','linkden','status')