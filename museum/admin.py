from django.contrib import admin

from museum.models import Museum, Gallery


@admin.register(Museum)
class MuseumAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    ordering = ('active',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('created', 'museum', 'title',)
    list_display_links = ('created', 'museum', 'title',)
    list_filter = ('created',)
    search_fields = ('title',)
