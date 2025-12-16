from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book
from library.serializers import BookSerializer


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    return Response({"massage": "Wellcome to Library API"})

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# ...................ViewSet..........................

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

