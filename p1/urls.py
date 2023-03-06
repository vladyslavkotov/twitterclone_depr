"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tweets.views import TweetListView,TweetDetailView,TweetCreateView,UserTweetListView

from users.views import UserCreateView,UserDetailView,follow
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import CustomAuthenticationForm

urlpatterns = [ #rewrite using include for tweets and users
    path('admin/', admin.site.urls),
    # path('',include('tweets.urls')),
    path('feed/', TweetListView.as_view(), name='feed'),
    path('<author>/tweets', UserTweetListView.as_view(), name='userfeed'),
    path('<author>/<int:pk>/', TweetDetailView.as_view(),name='detail'),
    path('register/', UserCreateView.as_view(),name='register'),
    path('<int:pk>/reply/', TweetCreateView.as_view(),name='create'),
    path('follow/',follow, name='follow'),
    # path('profile/', UserDetailView.as_view(),name='profile'),
    path('login/', LoginView.as_view(template_name="users/login.html",authentication_form=CustomAuthenticationForm),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),

]
