from rest_framework import serializers
from .models import Movie, Review, Director

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'content', 'stars']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return None
        return sum(review.stars for review in reviews) / reviews.count()

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movies.count()

