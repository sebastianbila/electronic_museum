from django import template

from ..models import EventSubscribers

register = template.Library()


@register.simple_tag
def total_subs():
    return EventSubscribers.objects.count()