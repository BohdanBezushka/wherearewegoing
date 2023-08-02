from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import UserDataForm

# This is the web page when the user wants to buy ticktes.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('festivals'))

    userdata_form = UserDataForm()
    template = 'checkout/checkout.html'
    context = {
        'userdata_form': userdata_form,
    }

    return render(request, template, context)
