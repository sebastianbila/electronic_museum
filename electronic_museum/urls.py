from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('museum', include('museum.urls', namespace='museum')),
    path('accounts/', include('accounts.urls')),
    path('news/', include('news.urls', namespace='news')),
    path('events/', include('events.urls', namespace='events')),
    path('books/', include('books.urls', namespace='books')),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
