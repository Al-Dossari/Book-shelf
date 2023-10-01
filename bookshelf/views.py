from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


from rest_framework.views import APIView
from rest_framework.response import Response

import requests


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInfoView(APIView):
    def get(self, request, isbn):
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if f"ISBN:{isbn}" in data:
                book_data = data[f"ISBN:{isbn}"]

                title = book_data.get('title', '')
                author = book_data.get('authors', [{'name': ''}])[0]['name']
                book = Book(title=title, author=author)
                book.save()

                return Response(book_data)
            else:
                return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Unable to fetch book data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookSearchView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        title = self.kwargs.get('title')
        obj = Book.objects.get(title=title)
        return obj


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookEditSeralizer


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Book.objects.get(pk=pk)

