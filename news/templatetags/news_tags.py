from django import template
from django.shortcuts import get_object_or_404

from ..models import News

register = template.Library()


@register.simple_tag
def get_latest_news(count=5):
    return News.published.order_by('-publish')[:count]


@register.inclusion_tag('partials/_modal_comments.html')
def load_comments(news, pk):
    news = get_object_or_404(News,
                             id=pk,
                             slug=news,
                             status='published')

    return {'comments': news.comments.filter(active=True).order_by('-created')}
