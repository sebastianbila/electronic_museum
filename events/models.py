from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Event(models.Model):
    STATUS_CHOICES = (
        ('overdue', 'Overdue'),
        ('active', 'Active'),
    )

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='events/', blank=True)
    slug = models.SlugField(max_length=150)
    description = models.TextField(max_length=850, default='')
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=300)
    author = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='active')

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        verbose_name_plural = 'Master Classes'
        verbose_name = 'Master Class'
        ordering = ('created',)
        db_table = 'events'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail',
                       args=[self.slug, self.id])


class EventSubscribers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='subscribers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_user')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Event Subscribers'
        ordering = ('created',)
        db_table = 'event_subscribers'
