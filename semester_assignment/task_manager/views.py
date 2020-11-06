from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts
    
def create_post(request):
    return render(request, 'task_manager/create_post.html')

def main_page(request):
    context = {
        "tasks": Posts.objects.all()
    }

    return render(request, 'task_manager/main_page.html', context)

def settings(request):
    return render(request, 'task_manager/settings.html')

def login(request):
    return render(request, 'task_manager/login.html')

def dashboard(request):
    return render(request, 'task_manager/dashboard.html')

