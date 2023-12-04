from django import forms
from self_profile.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'student_id', 'major', 'username', 'email']
