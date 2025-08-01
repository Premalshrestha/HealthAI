from django.contrib import admin
from django.contrib.auth.models import User,Group
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

admin.site.unregister(Group)
#Mix profile info imto user user info
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'



class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','email','password']
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
