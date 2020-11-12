from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Posts
    template_name = 'task_manager/main_page.html'
    context_object_name = 'tasks'
    ordering = ['-datetime_posted']


class PostDetailView(DetailView):
    model = Posts
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['general_description', 'is_important', 'is_completed', 'expertise']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['general_description', 'is_important', 'is_completed', 'expertise']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def create_post(request):
    return render(request, 'task_manager/create_post.html')

def main_page(request):
    context = {
        "tasks": Posts.objects.all(),
    }

    return render(request, 'task_manager/main_page.html', context)

def settings(request):
    return render(request, 'task_manager/settings.html')

def login(request):
    return render(request, 'task_manager/login.html')

def dashboard(request):
    return render(request, 'task_manager/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able ot login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'task_manager/register.html', {'form' : form})

