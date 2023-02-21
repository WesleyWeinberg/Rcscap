from django.shortcuts import render
from .models import PromoName,Meeting,Event

def index(request):
    """The home page for RCSS."""
    names = PromoName.objects.order_by('date_added')
    meetings = Meeting.objects.order_by('meeting_date')
    events = Event.objects.order_by('event_date')
    context = {'names': names, 'meetings':meetings, 'events':events}
    return render(request, 'sitepages/index.html', context)

