from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Book  # Assuming you have a Book model
from .serializers import BookSerializer  # Assuming you have a BookSerializer

# Sample view for handling GET requests to list all books or books by a specific author
class BookList(APIView):
    def get(self, request):
        # Get the 'author' parameter from the query string
        author = request.GET.get("author", None)
        
        if author:
            # If an author is provided, filter books by author (case-insensitive search)
            books = Book.objects.filter(author__icontains=author)
        else:
            # Otherwise, return all books
            books = Book.objects.all()

        # Serialize the books and return them in the response
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new book (this part might need more implementation)
        return Response({"message": "New book created"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def books(request):
    # Just a simple placeholder function for now
    return Response("list of the books", status=status.HTTP_200_OK)

class Book(APIView):
    def get(self,request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title":request.data.get("title")}, status.HTTP_200_OK)