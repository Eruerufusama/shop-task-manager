from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

class PostListView(ListView):#With this posts will be ordered from oldest to newest from the bottom to the top. Like a twitter feed.
    model = Posts
    template_name = 'task_manager/main_page.html'
    context_object_name = 'tasks'
    ordering = ['-datetime_posted']



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

