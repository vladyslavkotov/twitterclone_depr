from django.contrib import admin
from tweets.models import Tweet
from django.utils.translation import gettext_lazy as _

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ["pk","text","author","date_posted"]
    # fields=["text","author","pic1"]

admin.site.register(Tweet,TweetAdmin)