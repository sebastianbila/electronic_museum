from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('', views.EventListView.as_view(), name='home'),
    path('<slug:event>/<int:pk>/', views.event_detail, name='event_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
