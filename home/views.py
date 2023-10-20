from django.shortcuts import render, redirect
from .models import ContactForm
from .forms import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ A view on the company """

    return render(request, 'home/about_us.html')


def contact(request):
    """ Contact for issues with tickets"""

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            form.save()
            messages.success(request, f'The form has been successfully submitted. We will not take long to get in touch with you. Thank you, {name}!')
            return redirect(request.path)
    else:
        form = Contact()

    return render(request, 'home/contact.html', {'form': form})

def newsletter(request):
    """ Newsletter for users who want to be informed about new festivals, news..."""

    return render(request, 'home/newsletter.html')
