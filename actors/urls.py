from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

app_name = "actors"

urlpatterns = [
    path("actors/", ActorCreateListView.as_view(), name="create-list"),
    path(
        "actors/<int:pk>/", ActorRetrieveUpdateDestroyView.as_view(), name="detail-view"
    ),
]
