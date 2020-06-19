from django.urls import path
from apps.api.views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
]
