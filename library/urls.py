from django.urls import path

from library.views import api_overview, get_books

urlpatterns = [
    path('api/',api_overview),
    path('get_books', get_books)

]