from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator,URLValidator

# Create your models here.

class User(AbstractUser):

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
    link = models.CharField(max_length=50,blank=True,
        validators=[url_validator])
    userpic = models.ImageField(default='default.jpg', upload_to='userpics')
    background = models.ImageField(default='default.jpg', upload_to='backgrounds')
    is_verified = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)  # first created
    bio = models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
