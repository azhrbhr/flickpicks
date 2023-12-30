# from accounts.models import Profile
from django.contrib import admin


admin.site.site_header = 'FlickPicks Administration'
admin.site.index_title = 'Welcome to FlickPicks Administration'


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone_number', 'address']
#     search_fields = ['user__username']


# admin.site.register(Profile, ProfileAdmin)
