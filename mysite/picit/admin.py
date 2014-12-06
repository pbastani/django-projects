from django.contrib import admin
from picit.models import Image, Tag


class TagInline(admin.StackedInline):
    model = Tag
    extra = 5


class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',               {'fields': ['title']}),
        ('Url', {'fields': ['url'], 'classes': ['collapse']}),
    ]
    inlines = [TagInline]

admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)