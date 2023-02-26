from django.contrib import admin
from users.models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "name", "email","is_verified","joined",]
    readonly_fields = ["joined"]

    fieldsets = ((None, {"fields": ("username", "password","is_verified")}),
    (_("Personal info"),
        {"fields": ("name", "email", "link", "userpic","background","joined","bio","followers","following")}),
    (_("Permissions"),
     {"fields": ("is_active", "is_staff", "is_superuser", ), },), )

admin.site.register(User,UserAdmin)
