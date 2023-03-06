from django.db import models

from users.models import User

class Tweet(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=280)
    date_posted=models.DateTimeField(auto_now_add=True) #first created. can edit tweets with twitter blue only
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name='replied')
    pic1=models.ImageField(upload_to='tweetpics', blank=True)

    likes = models.ManyToManyField(User,symmetrical=False,related_name='tweet_likes')
    retweets = models.ManyToManyField(User,symmetrical=False,related_name='tweet_retweets')
    replies = models.ManyToManyField('self',symmetrical=False,related_name='tweet_replies')

    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk} {self.text} by {self.author} at {self.date_posted}"

    def save(self, *args, **kwargs):
        '''DONT call save() on self.replied_to
        add() and create() doesnt require save()'''
        super().save(*args,**kwargs)
        if self.replied_to:
            self.replied_to.replies.add(self)

