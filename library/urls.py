from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views import api_overview, get_books, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='BookViewSet')

urlpatterns = [
    path('api/',api_overview),
    path('get_books', get_books),

    path("", include(router.urls))
]