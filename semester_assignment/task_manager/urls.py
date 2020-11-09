from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name="main-page"),
    path('posts_detail/<int:pk>/', views.PostDetailView.as_view(), name="posts-detail"),
    path('create_post/', PostCreateView.as_view(), name="post-create"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
]