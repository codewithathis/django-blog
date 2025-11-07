from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    list_filter = ['created', 'published', 'author']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author_name', 'created', 'active']
    list_filter = ['active', 'created']
    
admin.site.register(Tag)