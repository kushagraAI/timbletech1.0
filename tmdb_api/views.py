from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Tmdb_Movie, Review, Comment
from .serializers import Tmdb_MovieSerializer, ReviewSerializer, CommentSerializer, UserSerializer
from django.contrib.auth.models import User
from tmdb_api.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class MoviePagination(PageNumberPagination):
    page_size = 10


class ReviewPagination(PageNumberPagination):
    page_size = 5


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Tmdb_Movie.objects.all()
    serializer_class = Tmdb_MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'overview']
    pagination_class = MoviePagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ReviewPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
