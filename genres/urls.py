from django.urls import path

from genres.views import genre_create_list_view, genre_detail_view

app_name = "genres"

urlpatterns = [
    path("", genre_create_list_view, name="create-list"),
    path("<int:pk>/", genre_detail_view, name="detail-view"),
]
