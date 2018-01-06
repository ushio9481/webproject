from django.contrib import admin
from .models import Post, Category, Tag, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    inlines = [PhotoInline]


admin.site.register(Photo)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

