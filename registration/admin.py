from django.contrib import admin
from registration.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('phone_number','home_address','user')

admin.site.register(UserProfile,UserProfileAdmin)

