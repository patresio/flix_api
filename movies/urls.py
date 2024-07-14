from django.urls import path

from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("", MovieCreateListView.as_view(), name="create-list"),
    path(
        "<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy",
    ),
]
