
from django.views.generic import ListView,DetailView,CreateView
from .models import User
from django.urls import reverse
from .admin import UserCreationForm, UserAuthenticationForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import *
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from tweets.models import Tweet
from users.models import User

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('feed')

class UserLoginView(LoginView):

    form_class = UserAuthenticationForm
    template_name = "users/login.html"

class UserLogoutView(LogoutView):

    form_class = UserAuthenticationForm
    template_name = "users/logout.html"

#toggles
def follow(request,pk):
    user = User.objects.get(pk=request.POST.get('user_pk'))
    if request.user in user.followers.all():
        request.user.following.remove(user)
        user.followers.remove(request.user)
    else:
        request.user.following.add(user)
        user.followers.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def like(request,pk):
    #even tho pk arg is not used, it IS used - we pass it from template
    tweet=Tweet.objects.get(pk=request.POST.get('tweet_pk'))
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def dislike(request,pk):
    #even tho pk arg is not used, it IS used - we pass it from template
    tweet=Tweet.objects.get(pk=request.POST.get('tweet_pk'))
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

# def retweet(request,pk):
#     tweet=Tweet.objects.get(pk=request.POST.get('tweet_pk'))
#     tweet.retweets.add(request.user)
#     tweet.pk=None
#     tweet.author=request.user
#     tweet.save()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])

def retweet(request,pk):
    tweet=Tweet.objects.get(pk=request.POST.get('tweet_pk'))
    tweet.retweets.add(request.user)
    new_tweet=Tweet.objects.create(author=request.user,replied_to=None,text=tweet.text,views=tweet.views)
    new_tweet.replies.add(*tweet.replies.all())
    new_tweet.likes.add(*tweet.likes.all())
    new_tweet.retweets.add(*tweet.retweets.all())
    return HttpResponseRedirect(request.META['HTTP_REFERER'])