from django.urls import path
from . import views



urlpatterns = [
    path('', views.main_page, name="main-page"),
    path('create_post/', views.create_post, name="create-post"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
]