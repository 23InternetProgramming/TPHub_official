from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django.urls import reverse
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		if self.user and self.user.is_authenticated:
			for event in events_per_day:
				d += f'<li> {event.get_html_url} </li>'
			if day != 0:
				return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		else:
			if day != 0:
				return f"<td><span class='date'>{day}</span><ul></ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		schedule = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		schedule += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		schedule += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			schedule += f'{self.formatweek(week, events)}\n'
		return schedule

	def get_delete_url(self, event):
		return reverse('schedule:event_delete', args=[event.id])