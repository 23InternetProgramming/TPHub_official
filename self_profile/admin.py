from django.contrib import admin
from .models import Post, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'student_id', 'major', 'email', 'phone_number','role', 'git', 'instagram',
                    'facebook')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post)
