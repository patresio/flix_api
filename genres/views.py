from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.permissions import GenrePermissionClass
from genres.serializers import GenreSerializer


# Create your views here.
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        GenrePermissionClass,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
        GenrePermissionClass,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
