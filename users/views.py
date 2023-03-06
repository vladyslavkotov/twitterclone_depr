
from django.views.generic import ListView,DetailView,CreateView
from .models import User
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('feed')

class UserDetailView(DetailView):
    model = User
    # form_class = CustomUserCreationForm

def follow(request):
    user_follower=request.user
    context={'follower':user_follower}
    return render(request,'users/follow.html',context)

# def like(request,id):

#should be toggles. cancel on click
