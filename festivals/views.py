from django.shortcuts import render, redirect, reverse, get_object_or_404
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
        """The user can search by price, location and date."""


        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                festivals = festivals.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            festivals = festivals.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('festivals'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            festivals = festivals.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'festivals': festivals,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'festivals/festivals.html', context)


def festival_detail(request, festival_id):
    """ A view to show individual festival details"""

    festival = get_object_or_404(Festival, pk=festival_id)

    context = {
        'festival': festival,
    }

    return render(request, 'festivals/festival_detail.html', context)
