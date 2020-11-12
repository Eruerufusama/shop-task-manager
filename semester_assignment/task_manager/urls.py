from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name="main-page"),
    path('posts_detail/<int:pk>/', views.PostDetailView.as_view(), name="posts-detail"),
    path('posts_detail/<int:pk>/update', views.PostUpdateView.as_view(), name="posts-update"),
    path('posts_detail/<int:pk>/delete', views.PostDeleteView.as_view(), name="posts-delete"),
    path('create_post/', PostCreateView.as_view(), name="post-create"),
    path('settings/', views.settings, name="settings"),
    path('dashboard/', views.dashboard, name="dashboard"),
]