import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre


# Create your views here.
@csrf_exempt
def genre_create_list_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return JsonResponse({"id": genre.id, "name": genre.name})
