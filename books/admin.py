from django.contrib import admin

from books.models import CategoryBook, Book


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    list_display_links = ('name', 'active',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created', 'active')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'author', 'pages', 'active',)
    list_display_links = ('category', 'name', 'author', 'pages', 'active',)
    list_filter = ('created', 'active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'author', 'body')
