from django.urls import path
from apps.books.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]
