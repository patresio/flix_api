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
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == "GET":
        return JsonResponse({"id": genre.id, "name": genre.name})
    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        genre.name = data["name"]
        genre.save()
        return JsonResponse({"id": genre.id, "name": genre.name})
    if request.method == "DELETE":
        genre.delete()
        return JsonResponse(
            {"message": "Genre deleted successfully"},
            status=204,
            safe=False,
            json_dumps_params={"ensure_ascii": True},
        )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
