from django.contrib import admin

# Register your models here.
from .models import Author, Post, Category

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
