from django.contrib import admin
from .models import *





class BlogAdmin(admin.ModelAdmin):
    list_display=('title','accepted','created','updated')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name','badge')


# admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)





