from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/', blank=True)
    slug = models.SlugField(max_length=150, unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='news')
    description = models.CharField(max_length=500)
    body = RichTextUploadingField(blank=False, null=False, config_name='news_editor')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'News'
        verbose_name = 'News'
        db_table = 'news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail',
                       args=[self.slug, self.id])


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.username} on {self.news}'
