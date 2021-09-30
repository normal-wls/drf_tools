from rest_framework.viewsets import ModelViewSet

from book_api_swagger.models import Book
from book_api_swagger.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
