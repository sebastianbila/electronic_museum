from django.contrib import admin

from newsletter.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed', 'unsubscribed',)
    list_display_links = ('email', 'subscribed', 'unsubscribed',)
    list_filter = ('subscribed',)
    search_fields = ('email',)
