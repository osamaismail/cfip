from django.contrib import admin
from .models import Profile



class UserLevelAdmin(admin.ModelAdmin):
    list_display=('user','level')


admin.site.register(Profile, UserLevelAdmin)
