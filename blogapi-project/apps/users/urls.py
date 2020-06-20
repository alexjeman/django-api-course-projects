from django.urls import path
from apps.users.views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
