from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
import pdb

from timeline.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event


class TimelineEvent:
    title = ""
    description = ""
    reference_url = ""
    icon_url = ""
    year = ""
    event_date = ""
    tags = []
    categories = []

    def __init__(self, title, description, reference_url, icon_url, tags, categories, section_date, event_date):
        self.title = title
        self.description = description
        self.reference_url = reference_url
        self.icon_url = icon_url
        self.tags = tags
        self.categories = categories
        self.section_date = section_date
        self.event_date = event_date.strftime("%b. %d")


def index(request):
    events = Event.objects.order_by("-date").all()
    timeline_events = []
    year = 0
    for event in events:
        event_year = 0
        if event.date.year != year:
            event_year = event.date.year
            year = event.date.year

        timeline_events.append(TimelineEvent(
            event.title,
            event.description,
            event.reference_url,
            event.icon_url,
            event.tags,
            event.categories,
            event_year,
            event.date))

    context = \
        {
            'events': timeline_events,
            'start': 1870,
            'end': 1880,
        }
    # pdb.set_trace()
    return render(request, 'timeline/index.html', context)