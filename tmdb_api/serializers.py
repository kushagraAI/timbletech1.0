from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tmdb_Movie, Review, Comment


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tmdb_Movie.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'movies']


class Tmdb_MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']
