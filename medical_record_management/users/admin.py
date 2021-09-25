from django.contrib import admin
from users import models


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'first_name',
        'last_name', 'security_level'
    ]
    search_fields = [
        'username', 'first_name', 'last_name',
        'email', 'security_level'
    ]


admin.site.register(models.User)
