from django.db import models

from users.models import User

class Tweet(models.Model):

    text=models.CharField(max_length=280)
    date_posted=models.DateTimeField(auto_now_add=True) #first created. can edit tweets with twitter blue only
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name='replied')
    pic1=models.ImageField(upload_to='tweetpics', blank=True)

    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    replies = models.ManyToManyField('self',symmetrical=False)

    def __str__(self):
        return f"{self.pk} {self.text} by {self.author} at {self.date_posted}"

    def save(self, *args, **kwargs):
        # DONT call save on self.replied_to
        super().save(*args,**kwargs)
        # print(self.replied_to, type(self.replied_to))
        self.replied_to.replies.add(self)

