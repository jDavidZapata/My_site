from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug', 'image')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
