from django.urls import path
from .views import PostListView
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name="main-page"),
    path('create_post/', views.create_post, name="create-post"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
]