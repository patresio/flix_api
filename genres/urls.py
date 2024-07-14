from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

app_name = "genres"

urlpatterns = [
    path("genres/", GenreCreateListView.as_view(), name="create-list"),
    path(
        "genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name="detail-view"
    ),
]
