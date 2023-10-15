from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ A view on the company """

    return render(request, 'home/about_us.html')


def contact(request):
    """ Contact for issues with tickets"""

    form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

def newsletter(request):
    """ Newsletter for users who want to be informed about new festivals, news..."""

    return render(request, 'home/newsletter.html')
