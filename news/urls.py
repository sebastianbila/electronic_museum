from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news'),
    path('tag/<slug:tag_slug>/', views.news_list, name='news_by_tag'),
    path('<slug:news>/<int:pk>/', views.news_detail, name='news_detail'),
]
