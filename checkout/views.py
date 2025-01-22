from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': 'pk_test_51QkA8y09i9j5PbfJ5uh5lxL8dTYtzNNwU3HSY7cOVxI22r0eGv9kWmq1euMGOOZqeeyqoITwZgsgYs5JH2F3W3gn00xS1KzXT8',
        'order_form': order_form,
    }

    return render(request, template, context)
