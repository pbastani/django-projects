from django.contrib import admin
from timeline.models import Event, Tag, Category


class TagInline(admin.StackedInline):
    model = Tag
    extra = 3


class CategoryInLine(admin.StackedInline):
    model = Category
    extra = 2


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
        ('Date', {'fields': ['date']}),
        ('Reference', {'fields': ['reference_url']}),
        ('Icon', {'fields': ['icon_url']}),
    ]
    inlines = [TagInline, CategoryInLine]

admin.site.register(Event, EventAdmin)
admin.site.register(Tag)
admin.site.register(Category)