# BookList/urls.py

from django.contrib import admin
from django.urls import path, include
from BookListAPI import views  # Make sure to import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListAPI.urls')),  # Include BookListAPI URLs under '/api/'
    path('', views.index, name='index'),  # Maps root URL to BookListAPI's index view
]
