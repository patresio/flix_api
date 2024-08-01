from django.urls import path

from movies.views import (
    MovieCreateListView,
    MovieRetrieveUpdateDestroyView,
    MovieStatsView,
)

app_name = "movies"

urlpatterns = [
    path("movies/", MovieCreateListView.as_view(), name="create-list"),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy",
    ),
    path("movies/stats/", MovieStatsView.as_view(), name="stats"),
]
