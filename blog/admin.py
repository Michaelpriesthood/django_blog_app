from django.contrib import admin
from . models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title',  'publish',]
    list_filter = ['publish']
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Comment)



