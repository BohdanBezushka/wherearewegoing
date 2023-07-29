from django.shortcuts import render, get_object_or_404
from .models import Festival

# Create your views here.


def all_festivals(request):
    """ A view to show all festivals and search queries """

    festivals = Festival.objects.all()

    context = {
        'festivals': festivals,
    }

    return render(request, 'festivals/festivals.html', context)

def festival_detail(request, festival_id):
    """ A view to show individual festival details"""

    festival = get_object_or_404(Festival, pk=festival_id)

    context = {
        'festival': festival,
    }

    return render(request, 'festivals/festival_detail.html', context)