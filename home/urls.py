from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('search/', views.search, name='search'),
]
