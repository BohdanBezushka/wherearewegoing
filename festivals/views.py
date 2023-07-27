from django.shortcuts import render
from .models import Festival

# Create your views here.


def all_festivals(request):
    """ A view to show all festivals and search queries """

    festivals = Festival.objects.all()
    print(festivals)

    context = {
        'festivals': festivals,
    }

    return render(request, 'festivals/festivals.html', context)
