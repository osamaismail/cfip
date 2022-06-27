from django.contrib import admin
from .models import Contact, Team




class ContactAdmin(admin.ModelAdmin):
    list_display=('fname','lname','email','created')




admin.site.register(Contact, ContactAdmin)
admin.site.register(Team)