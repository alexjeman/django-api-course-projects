from rest_framework import generics

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializers


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
