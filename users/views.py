
from django.views.generic import ListView,DetailView,CreateView
from .models import User
from django.urls import reverse
from .admin import UserCreationForm, UserAuthenticationForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('feed')

class UserDetailView(DetailView):
    model = User
    # form_class = CustomUserCreationForm

class UserLoginView(LoginView):

    form_class = UserAuthenticationForm

class UserLogoutView(LogoutView):

    form_class = UserAuthenticationForm

def follow(request):
    user_follower = request.user
    context = {'follower': user_follower}
    return render(request, 'users/follow.html', context)

def like(request):
    pass