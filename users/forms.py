from django.contrib.auth.forms import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    #removed help text, added fields
    password1 = forms.CharField(label=_("Password"),
            strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), )

    password2 = forms.CharField(label=_("Password confirmation"),
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), strip=False, )

    class Meta:
        model = User
        fields = ("username","email","name","password1","password2","bio","userpic")

class CustomAuthenticationForm(AuthenticationForm):
    #doesnt work. validates email but doest check if matches
    pass
    # email = forms.EmailField(label=_("Email"),
    #                          max_length=254,
    #                          widget=forms.EmailInput(attrs={"autocomplete": "email"}), )
    #
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #
    #     if username is not None and email is not None and password:
    #         self.user_cache = authenticate(
    #             self.request, username=username, email=email, password=password
    #         )
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #
    #     return self.cleaned_data