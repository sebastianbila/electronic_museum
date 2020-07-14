from django.contrib import admin
from events.models import Event, EventSubscribers


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'date', 'status')
    list_display_links = ('title', 'slug', 'author', 'date', 'status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('status', 'created')


@admin.register(EventSubscribers)
class EventSubscribersAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'created',)
    list_display_links = ('event', 'user', 'created',)
    list_filter = ('event', 'user', 'created')
    search_fields = ('event', 'user')
