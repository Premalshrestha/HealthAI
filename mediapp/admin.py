from django.contrib import admin
from .models import UserProfile,Family


admin.site.site_header = "MediMate Admin"
admin.site.site_title = "MediMate Admin Portal"
admin.site.index_title = "Welcome to MediMate Admin Portal"



admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth','user']


admin.site.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
