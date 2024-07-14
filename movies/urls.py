from django.urls import path

from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

app_name = "movies"

urlpatterns = [
    path("movies/", MovieCreateListView.as_view(), name="create-list"),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy",
    ),
]
