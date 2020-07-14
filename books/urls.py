from django.contrib import admin
from django.urls import path, include
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.CategoryBooksListView.as_view(), name='home'),
    path('<slug:book>/<int:pk>/', views.BooksListView.as_view(), name='books_detail'),
    path('<slug:category>/<slug:book>/<int:pk>/', views.book_single, name='book_single'),

]
