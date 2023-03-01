from django.contrib import admin
from users.models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["pk","username", "name", "email","is_verified","date_joined","last_login"]
    readonly_fields = ["date_joined","last_login"]

    fieldsets = ((None, {"fields": ("username", "password", "is_verified")}),
    (_("Personal info"),
        {"fields": ("name", "email", "link", "userpic","background",
                    "date_joined","last_login","bio",)}),
    (_("Follow"),
     {"fields": ("followers", "following", ), },),
                 )

admin.site.register(User,UserAdmin)
