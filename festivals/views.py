from django.shortcuts import render
from .models import Festical

# Create your views here.


def all_festivals(request):
    """ A view to show all festivals, including sorting and search queries """

    festivals = Festival.objects.all()

    context = {
        'festivals': gestivals,
    }

    return render(request, 'festivals/festivals.html', context)