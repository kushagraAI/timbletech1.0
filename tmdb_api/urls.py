from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, CommentViewSet, CustomAuthToken
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name='auth-token'),
]
