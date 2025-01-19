# BookListAPI/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('books/', views.books, name='books'),  # Map /api/books to the books view
    path("books/", views.BookList.as_view(), name="book-list"),
]
