from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializers(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, obj):
        return obj.movies.count()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieReviewSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews average_rating'.split()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

class DirectorValidatorSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=25)
    description = serializers.CharField(min_length=5, max_length=1500)
    duration = serializers.FloatField(min_value=1, max_value=5)
    director_id = serializers.IntegerField()

class ReviewValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=1500)
    movie_id = serializers.IntegerField()

class DirectorDetailValidatorSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieDetailValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=25)
    description = serializers.CharField(min_length=5, max_length=1500)
    duration = serializers.FloatField(min_value=1, max_value=5)
    director_id = serializers.IntegerField()

class ReviewDetailValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=1500)
    movie = serializers.CharField()
    movie_id = serializers.IntegerField()





