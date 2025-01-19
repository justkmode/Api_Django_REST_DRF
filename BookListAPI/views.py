# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        return Response({"message": "List of books as JSON"})
    elif request.method == 'POST':
        # Handle the POST request and add book logic
        return Response({"message": "Book added"})
