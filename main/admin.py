from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User

# Register your models here.

admin.site.site_header = "Juan's Site Administration"
admin.site.site_title = "Code Adventure"
admin.site.index_title = "Admin"

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass