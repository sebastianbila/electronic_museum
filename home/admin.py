from django.contrib import admin

from home.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created',)
    list_display_links = ('name', 'email', 'message', 'created',)
    list_filter = ('created', 'email')
    search_fields = ('name', 'email', 'message')
