from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()
