from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)

admin.site.register(Comment)
