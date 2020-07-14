from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Museum(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='museum/')
    slug = models.SlugField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name_plural = 'Museum'
        ordering = ('created',)
        db_table = 'museum'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('museum:gallery',
                       args=[self.slug, self.id])


class Gallery(models.Model):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name='gallery')
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='museum/{}/'.format(museum))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ('created',)

    def __str__(self):
        return self.title

