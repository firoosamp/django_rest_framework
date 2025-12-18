from django.db import models
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Borrower, Author
from library.serializers import BookSerializer, BorrowerSerializer, AutherSerializer


# Create your views here.

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


@api_view(['GET'])
def api_overview(request):
    return Response({"massage": "Wellcome to Library API"})

# @api_view(['GET'])
# def get_books(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# ...................ViewSet..........................

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsStaffOrReadOnly]


    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['author', 'published_date']
    search_fields = ['title', 'author']
    ordering_fields = ['price', 'published_date']


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

    permission_classes = [IsStaffOrReadOnly]


    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['name', 'borrowed_books']
    search_fields = ['name', 'borrowed_books']
    # ordering_fields = ['id', 'published_date']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer
    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['name', 'email']
    # filterset_fields = ['name', 'borrowed_books']
    # ordering_fields = ['id', 'published_date']