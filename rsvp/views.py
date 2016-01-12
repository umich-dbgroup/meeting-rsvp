import datetime as dt

from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rsvp.models import Event, Rsvp


class EventListView(ListView):
    model = Event
    def get_queryset(self, **kwargs):
        return Event.objects.order_by('-date', 'name')
        # .filter(date__gte=dt.datetime.today())

class RsvpCreateView(CreateView):
    model = Rsvp
    fields = ['name', 'vegetarian',]
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        event = Event.objects.get(pk=self.kwargs['event_id'])
        form.instance.event = event
        return super(RsvpCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(RsvpCreateView, self).get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['event_id'])
        ctx['event'] = event
        return ctx

class RsvpListView(LoginRequiredMixin, ListView):
    model = Rsvp
    def get_queryset(self, **kwargs):
        return Rsvp.objects.filter(event__id=self.kwargs['event_id'])\
                           .order_by('name')

    def get_context_data(self, **kwargs):
        ctx = super(RsvpListView, self).get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['event_id'])
        ctx['event'] = event
        return ctx
