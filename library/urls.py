from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from library.models import Borrower
from library.views import api_overview, BookViewSet, BorrowerViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='BookViewSet')
router.register(r'borrower', BorrowerViewSet, basename='BorrowerViewSet')
router.register(r'author', AuthorViewSet, basename='AuthorViewSet')
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',api_overview),

    path("", include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)