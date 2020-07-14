from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class CategoryBook(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category_books/')
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)
        db_table = 'category_books'

    def get_absolute_url(self):
        return reverse('books:books_detail',
                       args=[self.slug, self.id])


class Book(models.Model):
    category = models.ForeignKey(CategoryBook, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books/')
    slug = models.SlugField(max_length=250)
    author = models.CharField(max_length=500)
    body = RichTextUploadingField(blank=False, null=False, config_name='books_editor')
    pages = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)
        db_table = 'books'

    def get_absolute_url(self):
        return reverse('books:book_single',
                       args=[self.category.slug, self.slug, self.id])
