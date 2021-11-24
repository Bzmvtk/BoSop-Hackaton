from django.db import router
from django.urls import path, include
# from application.posts.views import CategoryView
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('post-list/', PostListView.as_view()),
    path('post-create/', PostCreateView.as_view()),
    path('post-update/<int:pk>/', PostUpdateView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
    path('', include(router.urls))
]