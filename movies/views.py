from django.db.models import Avg, Count
from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import (
    MovieListDetailSerializer,
    MovieModelSerializer,
    MovieStatsSerializer,
)
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()

    def get(self, request):
        # Buscar todos os dados
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"]
        # Montar resposta
        movie_stats = {
            "total_movies": total_movies,
            "movies_by_genre": movies_by_genre,
            "total_reviews": total_reviews,
            "average_stars": round(average_stars, 1) if average_stars else 0,
        }

        serializer = MovieStatsSerializer(data=movie_stats)
        serializer.is_valid(raise_exception=True)
        # Devolve resposta pro user com estatisticas
        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
