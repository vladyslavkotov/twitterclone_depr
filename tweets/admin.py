from django.contrib import admin
from tweets.models import Tweet
from django.utils.translation import gettext_lazy as _

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet,TweetAdmin)