from django import template

from ..models import Newsletter

register = template.Library()


@register.simple_tag
def is_subscribed(request):
    user = request.user
    if user is not None and not user.is_anonymous:
        email = user.email
        if Newsletter.objects.filter(email=email).exists():
            return True
        else:
            return False
    return False
