from django.db import models

from users.models import User

class Tweet(models.Model):

    text=models.CharField(max_length=280)
    when=models.DateTimeField(auto_now_add=True) #first created. can edit tweets with twitter blue only
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    replied_to = models.OneToOneField(User, on_delete=models.CASCADE, related_name="replied_to", default=User.objects.get(username='dummy'))
    pic1=models.ImageField(upload_to='tweetpics', blank=True)
    replies=models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} by {self.author} at {self.when}"