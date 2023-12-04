from calendar import calendar
import calendar
from datetime import datetime, date, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe

from .forms import EventForm
from .models import *
from .utils import Calendar

def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, "schedule/base.html", content)

def create_todo(request):
    user_input_str = request.POST['todoContent']
    # author이 자동으로 채워지도록 코드 추가
    author = request.user
    new_todo = Todo(content=user_input_str, author=author)
    new_todo.save()
    return HttpResponseRedirect(reverse('schedule:calendar'))

def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    print('삭제한 todo의 id', delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('schedule:calendar'))

class EventDeleteView(generic.DeleteView):
    model = Event
    template_name = 'schedule/event_confirm_delete.html'
    success_url = '/schedule/'

class CalendarView(generic.ListView):
    model = Event
    template_name = 'schedule/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        today = datetime.today().date()
        d = get_date(self.request.GET.get('month', str(today.year) + '-' + str(today.month))) ## ('day', None)

        # Instantiate our calendar class with today's year and date
        schedule = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_schedule = schedule.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_schedule)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        ##
        # Pass the URLs with updated month to the template
        context['prev_month_url'] = f"{reverse('schedule:calendar')}?{context['prev_month']}"
        context['next_month_url'] = f"{reverse('schedule:calendar')}?{context['next_month']}"

        # Pass today's date to the template
        context['today'] = today

        # Get todos and pass them to the template
        todos = Todo.objects.all()
        context['todos'] = todos

        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('schedule:calendar'))
    return render(request, 'schedule/event.html', {'form': form})
