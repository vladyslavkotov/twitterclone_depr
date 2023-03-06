from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from users.models import User
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import Tweet

class TweetListView(ListView):
    #feed for currently logged in user. no replies
    context_object_name = "tweets"
    model=Tweet

    # #tweets by only currently logged in user
    # def get_queryset(self):
    #     return Tweet.objects.filter(author=self.request.user)

    def get_queryset(self):
        #get current user
        current_user=User.objects.get(username=self.request.user)
        return Tweet.objects.filter(replied_to__isnull=True).filter(author__in=current_user.following.all())

class UserTweetListView(ListView):
    #need pagination here
    #profile page, user data and feed, follow/unfollow

    model=Tweet
    context_object_name = "tweets"
    template_name = "tweets/user_tweet_list.html"

    #works
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['author'])
        return Tweet.objects.filter(author=user)

class TweetDetailView(DetailView):
    #single tweet, replies and Reply form
    model=Tweet
    context_object_name = "tweet"

class TweetCreateView(LoginRequiredMixin,CreateView):
    model=Tweet
    context_object_name = "tweet"
    fields=["text","pic1"]

    def get_success_url(self):
        return reverse('feed')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)