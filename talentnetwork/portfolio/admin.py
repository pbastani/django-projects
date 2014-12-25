from django.contrib import admin
from .models import User, Photo, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Photo', {'fields': ['file']}),
        ('Views', {'fields': ['views']}),
        ('Uploaded On', {'fields': ['upload_date']}),
    ]
    inlines = [CommentInline]


class PhotoInLine(admin.StackedInline):
    model = Photo
    extra = 3


class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]
    inlines = [PhotoInLine]

# admin.site.register(Portfolio)
# admin.site.register(Portfolio, PortfolioAdmin)
# admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Comment)