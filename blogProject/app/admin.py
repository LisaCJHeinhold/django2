from django.contrib import admin

# Register your models here.
from .models import Post

# model for posts on admin view
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)