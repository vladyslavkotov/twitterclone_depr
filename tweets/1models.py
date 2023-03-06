from django.db import models

from users.models import User

#see if any of these fields should be unique but arent

class Tweet(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=280)
    date_posted=models.DateTimeField(auto_now_add=True) #first created. can edit tweets with twitter blue only
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name='replied')
    pic1=models.ImageField(upload_to='tweetpics', blank=True)
    pic2 = models.ImageField(upload_to='tweetpics', blank=True)
    pic3 = models.ImageField(upload_to='tweetpics', blank=True)
    pic4 = models.ImageField(upload_to='tweetpics', blank=True)

    likes = models.ManyToManyField(User,symmetrical=False,related_name='tweet_likes')
    retweets = models.ManyToManyField(User,symmetrical=False,related_name='tweet_retweets')
    replies = models.ManyToManyField('self',symmetrical=False,related_name='tweet_replies')
    bookmarks = models.ManyToManyField('self', symmetrical=False, related_name='tweet_replies')

    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk} {self.text} by {self.author} at {self.date_posted}"

    def save(self, *args, **kwargs):
        '''DONT call save() on self.replied_to
        add() and create() doesnt require save()'''
        super().save(*args,**kwargs)
        if self.replied_to:
            self.replied_to.replies.add(self)

class TweetList(models.Model):
    '''
    basically filtered feed. create list, add users. list might be pinned or not
    clicking on the same list a person is already in actually removes them from the list. bullshit
    you can get a person into a list but not follow them. might ignore this, such a minor detail

    then to read lists, get listview

    def get_queryset(self):

    current_user=User.objects.get(username=self.request.user)
    users_in_list=List.objects.get(pk=).users.all()
    return Tweet.objects.filter(replied_to__isnull=True).filter(author__in=users_in_list.all())
    '''

    name=models.CharField(max_length=50)
    tweets = models.ManyToManyField(User,symmetrical=False,related_name='tweetlist')
    is_pinned = models.BooleanField(default=False)

class Message(models.Model):
    '''conversations. listview for users
    for user in users

    def get_queryset(self):

    current_user=User.objects.get(username=self.request.user)
    users_in_list=List.objects.get(pk=).users.all()
    return Tweet.objects.filter(replied_to__isnull=True).filter(author__in=users_in_list.all())

    why not create conversation model? then it wont be doubling messages for both sender and receiver

    '''

    #cant be null. probably better to set to 'deleted account' on delete
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    #no idea
    is_sent = models.BooleanField(default=False)
    if_read = models.BooleanField(default=False)

class User(AbstractUser):

    #there is no phone number validator

    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()
    url_validator=URLValidator()

    username = models.CharField(_("username"),
        max_length=15,
        unique=True,
        help_text=_("Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists."), },
        )

    email = models.EmailField(_('email'),
        unique=True,
        error_messages={"unique": _("A user with that email already exists."), },
        validators=[email_validator],
        )

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50,blank=True, validators=[url_validator])
    userpic = models.ImageField(default='default.jpg', upload_to='userpics')
    background = models.ImageField(default='default.jpg', upload_to='backgrounds')
    is_verified = models.BooleanField(default=False)

    blocked=models.ManyToManyField('self',symmetrical=False, related_name='user_blocked')
    muted=models.ManyToManyField('self',symmetrical=False, related_name='user_muted')

    bio = models.TextField(max_length=160,blank=True)

    followers=models.ManyToManyField('self',symmetrical=False, related_name='user_followers')
    following = models.ManyToManyField('self',symmetrical=False, related_name='user_following')

    def __str__(self):
        return f'{self.username}'



