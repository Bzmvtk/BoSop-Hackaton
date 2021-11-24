from .models import SomePosts
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsQuestionAuthor
from rest_framework import generics


#CRUD for posts
class PostListView(generics.ListAPIView):
    queryset = SomePosts.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = SomePosts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]


class PostUpdateView(generics.UpdateAPIView):
    queryset = SomePosts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]


class PostDeleteView(generics.DestroyAPIView):
    queryset = SomePosts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]


