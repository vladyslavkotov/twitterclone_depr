from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator,URLValidator

class User(AbstractUser):
    #add phone

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
    bio = models.TextField(max_length=160,blank=True)

    followers=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,related_name='+')
    following = models.ForeignKey('self', on_delete=models.SET_NULL,null=True,related_name='+')

    def __str__(self):
        return f'{self.username}'
