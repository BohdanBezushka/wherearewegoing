from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Festival
from .forms import FestivalForm


# Create your views here.
def all_festivals(request):
    """ A view to show all festivals and search queries """

    festivals = Festival.objects.all()
    query = None
    sort = None
    direction = None

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
                messages.error(request, "You didn't enter \
                    any search criteria!")
                return redirect(reverse('festivals'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
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


@login_required
def add_festival(request):
    """ Add a festival to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES)
        if form.is_valid():
            festival = form.save()
            messages.success(request, 'Successfully added festival!')
            return redirect(reverse('festival_detail', args=[festival.id]))
        else:
            messages.error(request, 'Failed to add festival. \
                Please ensure the form is valid.')
    else:
        form = FestivalForm()

    form = FestivalForm()
    template = 'festivals/add_festival.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_festival(request, festival_id):
    """ Edit a festival in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    festival = get_object_or_404(Festival, pk=festival_id)
    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES, instance=festival)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated festival!')
            return redirect(reverse('festival_detail', args=[festival.id]))
        else:
            messages.error(request, 'Failed to update festival. \
                Please ensure the form is valid.')
    else:
        form = FestivalForm(instance=festival)
        messages.info(request, f'You are editing {festival.name}')

    template = 'festivals/edit_festival.html'
    context = {
        'form': form,
        'festival': festival,
    }

    return render(request, template, context)


@login_required
def delete_festival(request, festival_id):
    """ Delete a festival from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    festival = get_object_or_404(Festival, pk=festival_id)
    festival.delete()
    messages.success(request, 'Festival deleted!')
    return redirect(reverse('festivals'))
