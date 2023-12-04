from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from self_profile.models import UserProfile


class ExtendedUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            # UserProfile 모델에 저장
            UserProfile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                student_id='',
                major='',
                email=self.cleaned_data['email'],
                phone_number='',
                role='',
                git='',
                instagram='',
                facebook=''
            )
        return user
