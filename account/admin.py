from django.contrib import admin
from account.models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'photo', 'website', 'bio', 'phone', 'city', 'country',
                    'organization', 'is_tasker', 'is_expert')
    list_filter = ('gender', 'city', 'country', 'is_tasker', 'is_expert')
    ordering = ('gender', 'city', 'country', 'is_tasker', 'is_expert')
admin.site.register(Profile, ProfileAdmin)