from typing import Literal
from django.contrib import admin
from .models import Post


# Customise the admin panel to look more efficient
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ['title', 'content']

# Register your models here.
admin.site.register(Post, PostAdmin)