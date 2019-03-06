from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,

    PostCreateView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]
