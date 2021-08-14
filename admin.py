from django.contrib import admin
from .models import Blog,BlogCategory,BlogSeries
from tinymce.widgets import TinyMCE
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["blog_title", "blog_published"]}),
        ("URL", {'fields': ["blog_slug"]}),
        ("Series", {'fields': ["blog_series"]}),
        ("Content", {"fields": ["blog_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
admin.site.register(BlogSeries)
admin.site.register(BlogCategory)
admin.site.register(Blog,BlogAdmin)

# Register your models here.
