# BookListAPI/views.py

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Using the @api_view decorator
@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        # Here you can retrieve books from the database or just return a sample response
        return Response({"message": "List of books"})

    elif request.method == 'POST':
        # Here you can handle book creation (for simplicity, returning a dummy response)
        return Response({"message": "Book created successfully!"}, status=201)
