from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Account


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Account, UserAdmin)
