from django.contrib import admin
from .models import *



class NewsAdmin(admin.ModelAdmin):
    list_display=('title','accepted','created','updated')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name','badge')


# admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
