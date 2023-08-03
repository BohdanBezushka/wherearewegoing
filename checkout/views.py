from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import UserDataForm
from .models import UserData, Ticketing
from festivals.models import Festival
from bag.contexts import bag_contents

import stripe
import json

# This is the web page when the user wants to buy ticktes.

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'phone_number': request.POST['phone_number'],
            'email': request.POST['email'],
            'user_id': request.POST['user_id'],
            'date_of_birth': request.POST['date_of_birth'],
        }
        userdata_form = UserDataForm(form_data)
        if userdata_form.is_valid():
            order = userdata_form.save()
            for item_id, item_data in bag.items():
                try:
                    festival = Festival.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        ticketing = Ticketing(
                            order=order,
                            festival=festival,
                            quantity=item_data,
                        )
                        ticketing.save()
                except Festival.DoesNotExist:
                    messages.error(request, (
                        "One of the festivals in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print(userdata_form.errors)
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment.")
            return redirect(reverse('festivals'))

        userdata_form = UserDataForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'userdata_form': userdata_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(UserData, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)