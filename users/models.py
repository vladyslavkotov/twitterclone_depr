from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator, URLValidator
from django.utils.deconstruct import deconstructible
from django.contrib.auth.base_user import BaseUserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password

@deconstructible
class UsernameValidator(RegexValidator):
    regex = r'(?=\w{4,})(?!^\d)'
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and underscores"
    )
    flags = 0

@deconstructible
class EmailValidator(RegexValidator):
    regex = r'(?=\w+@[a-zA-Z]{2,}\.[a-zA-Z]{2,})(?=^[a-zA-Z])'
    message = _(
        "Enter a valid email"
    )
    flags = 0

class User(AbstractUser):
    #add phone

    username_validator = UsernameValidator()
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

    followers=models.ManyToManyField('self',symmetrical=False, related_name='user_followers')
    following = models.ManyToManyField('self',symmetrical=False, related_name='user_following')

    def __str__(self):
        return f'{self.username}'

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError("username required")
        if not email:
            raise ValueError("email required")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)