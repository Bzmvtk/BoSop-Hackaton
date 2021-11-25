from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
import django_filters
from rest_framework.pagination import PageNumberPagination

from .permissions import IsQuestionAuthor
from .serializer import PostSerializer
from .models import SomePosts

class PostFilter(django_filters.FilterSet):
    author = django_filters.NumberFilter(field_name='author_id')

    class Meta:
        model = SomePosts
        fields = ['author_id', ]

#CRUD for posts
class PostListView(generics.ListAPIView):
    queryset = SomePosts.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filter_class = PostFilter
    search_fields = ['title', ]

    def get_serializer_context(self):
        return {'request': self.request}


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

