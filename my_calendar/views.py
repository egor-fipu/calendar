from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import EventForm
from .models import Event


class EventsList(ListView):
    model = Event
    template_name = 'my_calendar/index.html'


class NewEvent(CreateView):
    form_class = EventForm
    success_url = reverse_lazy('index')
    template_name = 'my_calendar/new_event.html'
