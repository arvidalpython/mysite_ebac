from django.contrib import admin
from .models import Post

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status', 'created_on')
    list_filter = ('status','created_on')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)