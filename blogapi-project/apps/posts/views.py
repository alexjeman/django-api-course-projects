from rest_framework import generics, permissions
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.posts.permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
