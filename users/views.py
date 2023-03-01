
from django.views.generic import ListView,DetailView,CreateView
from .models import User
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('feed')

class UserDetailView(DetailView):
    model = User
    # form_class = CustomUserCreationForm