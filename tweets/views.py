from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from users.models import User
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import Tweet

class TweetListView(ListView):
    context_object_name = "tweets"
    model=Tweet

    # #tweets by only currently logged in user
    # def get_queryset(self):
    #     return Tweet.objects.filter(author=self.request.user)

    def get_queryset(self):
        mother_tweet=Tweet.objects.get(pk=1)
        return Tweet.objects.filter(replied_to=None)

class UserTweetListView(ListView):

    model=Tweet
    context_object_name = "tweets"
    template_name = "tweets/user_tweet_list.html"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['author'])
        return Tweet.objects.filter(author=user)

class TweetDetailView(DetailView):
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