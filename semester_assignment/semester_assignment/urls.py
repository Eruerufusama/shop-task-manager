from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from task_manager import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_manager.urls')),
    path('register/', task_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='task_manager/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='task_manager/logout.html'), name='logout'),

]
