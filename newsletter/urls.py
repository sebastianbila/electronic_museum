from django.urls import path
from newsletter import views

app_name = 'newsletter'

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
]
