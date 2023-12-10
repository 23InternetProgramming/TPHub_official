from django.views.generic import ListView
from schedule.models import Todo
from .models import Landing
from self_profile.models import UserProfile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class LandingList(ListView):
    #user_profile = UserProfile.objects.get(user=request.user)
    model = Landing
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todos = Todo.objects.all()
        context['todos'] = todos
        return context


@login_required
def base(request):
    user_id = request.session.get('user')
    if user_id:
        user_profile = UserProfile.objects.get(user=user_id)
    #user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'landing_page/base.html', {'user_profile': user_profile, 'user_id':user_id})
