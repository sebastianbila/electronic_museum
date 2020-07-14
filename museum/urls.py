from django.urls import path
from museum import views

app_name = 'museum'

urlpatterns = [
    path('', views.MuseumListView.as_view(), name='home'),
    path('<slug:museum_item>/<int:pk>/', views.gallery, name='gallery'),
]
