from django import template

from books.models import CategoryBook, Book
from events.models import Event
from news.models import News
from museum.models import Museum, Gallery

register = template.Library()


@register.inclusion_tag('home/latest_events.html')
def show_latest_events(count=3):
    obj = Event.active.order_by('-created')[:count]
    return {'events': obj}


@register.inclusion_tag('home/latest_news.html')
def show_latest_news(count=2):
    obj = News.published.order_by('-publish')[:count]
    return {'news': obj}


@register.inclusion_tag('home/latest_gallery.html')
def show_latest_gallery(count=7):
    museum = Museum.objects.filter(active=True)[:1]
    obj = Gallery.objects.filter(active=True, museum=museum)[:count]
    return {'gallery': obj}


@register.inclusion_tag('home/latest_books.html')
def show_latest_books(count=2):
    book = Book.objects.filter(active=True)[:count]
    return {'books': book}


@register.filter()
def class_name(value):
    return value.__class__.__name__


@register.inclusion_tag('search/search_item.html')
def search_item(obj):
    return {'obj': obj}
