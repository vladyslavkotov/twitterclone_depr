from django.db import models

from users.models import User

class Tweet(models.Model):
    #if tweet is not a reply, we need to create a dummy TWEET, NOT A USER, as a placeholder for self relationship
    #you reply to a tweet, not a user
    #linear O(n) lookup is absolutely out of the question.
    #the whole site will be exponentially slower as time progresses

    text=models.CharField(max_length=280)
    date_posted=models.DateTimeField(auto_now_add=True) #first created. can edit tweets with twitter blue only
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name='+')
    pic1=models.ImageField(upload_to='tweetpics', blank=True)

    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    replies = models.ManyToManyField('self')

    def __str__(self):
        return f"Tweet {self.text} by {self.author} at {self.date_posted}"