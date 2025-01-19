# In BookListAPI/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    # Other fields can be added as needed

    def __str__(self):
        return self.title
