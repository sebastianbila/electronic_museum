from django.contrib import admin

from news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_display_links = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'news', 'created', 'active')
    list_display_links = ('username', 'email', 'news', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('username', 'email', 'body')
