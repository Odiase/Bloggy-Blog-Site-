from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ("title",)}

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)