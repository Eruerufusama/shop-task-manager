from django.shortcuts import render

def create_post(request):
    return render(request, 'tast_manager/create_post.html')

def main_page(request):
    return render(request, 'task_manager/main_page.html')

def settings(request):
    return render(request, 'task_manager/settings.html')

def login(request):
    return render(request, 'task_manager/login.html')

def dashboard(request):
    return render(request, 'task_manager/dashboard.html')

