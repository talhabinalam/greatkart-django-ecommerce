from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.profile_picture:
            return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
        else:
            return object.user.email  # Change this line to use the desired attribute

    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'district', 'country')

    
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
