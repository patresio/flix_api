from django.urls import path

from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

app_name = "reviews"

urlpatterns = [
    path("", ReviewCreateListView.as_view(), name="create-list"),
    path("<int:pk>/", ReviewRetrieveUpdateDestroyView.as_view(), name="detail-view"),
]
