from django.shortcuts import render

tasks = [
    {
        "post_id": 0,
        "general_description": "Move these boxes!",
        "detailed Description": None,
        "is_important": False,
        "is_completed": False, 
        "time_stamp": "348535932762",
        "author": "5",
        "expertise": None
    },
    {
        "post_id": 1,
        "general_description": "Move these god damn boxes!",
        "detailed Description": None,
        "is_important": True,
        "is_completed": False, 
        "time_stamp": "348535933005",
        "author": "5",
        "expertise": None
    },
]

def create_post(request):
    return render(request, 'task_manager/create_post.html')

def main_page(request):
    context = {
        "Tasks": tasks
    }

    return render(request, 'task_manager/main_page.html', context)

def settings(request):
    return render(request, 'task_manager/settings.html')

def login(request):
    return render(request, 'task_manager/login.html')

def dashboard(request):
    return render(request, 'task_manager/dashboard.html')

