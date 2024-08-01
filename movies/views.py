from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermissions]
    queryset = Movie.objects.all()

    def get(self, request):
        # Buscar todos os dados
        # Montar resposta
        # Devolve resposta pro user com estatisticas
        return response.Response(
            data={"message": "Funcionou!"}, status=status.HTTP_200_OK
        )
