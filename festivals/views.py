from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Festival

# Create your views here.


def all_festivals(request):
    """ A view to show all festivals and search queries """

    festivals = Festival.objects.all()
    query = None

    """User can search in search bar"""
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('festivals'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            festivals = festivals.filter(queries)

    context = {
        'festivals': festivals,
        'search_term': query,
    }

    return render(request, 'festivals/festivals.html', context)

def festival_detail(request, festival_id):
    """ A view to show individual festival details"""

    festival = get_object_or_404(Festival, pk=festival_id)

    context = {
        'festival': festival,
    }

    return render(request, 'festivals/festival_detail.html', context)