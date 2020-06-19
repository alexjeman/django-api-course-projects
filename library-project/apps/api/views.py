from rest_framework import generics

from apps.books.models import Book
from apps.api.serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
