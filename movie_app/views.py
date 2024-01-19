from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializers, MovieSerializers, ReviewSerializers


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializers(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_api_view(request):
    if request.method =="GET":
        movies = Movie.objects.all()
        data = MovieSerializers(movies, many=True).data
        return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    if request.method =="GET":
        reviews = Review.objects.all()
        data = ReviewSerializers(reviews, many=True).data
        return Response(data=data)



@api_view(['GET'])
def director_detail_api_view(request, id):
    if request.method =="GET":
        directors = Director.objects.get(id=id)
        data = DirectorSerializers(directors).data
        return Response(data=data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    movies = Movie.objects.get(id=id)
    data = MovieSerializers(movies).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    reviews = Review.objects.get(id=id)
    data = ReviewSerializers(reviews).data
    return Response(data=data)