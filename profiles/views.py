from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import Wishlist, Product

@login_required
def profile(request):
    """ Display the user's profile along with wishlist and order history. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()  # Fetch user orders
    wishlist_items = Wishlist.objects.filter(user=request.user)  # Fetch wishlist

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,  # Pass wishlist to template
        'on_profile_page': True
    }

    return render(request, template, context)

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

@login_required
def add_to_wishlist(request, product_id):
    """Add product to the wishlist with a success message"""
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f"{product.name} has been added to your wishlist!")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")

    return redirect('profile')  # Redirect to profile page

@login_required
def remove_from_wishlist(request, product_id):
    """Remove product from the wishlist with a success message"""
    product = get_object_or_404(Product, id=product_id)

    if Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.filter(user=request.user, product=product).delete()
        messages.success(request, f"{product.name} has been removed from your wishlist.")
    else:
        messages.warning(request, f"{product.name} was not in your wishlist.")

    return redirect('profile')  # Redirect back to profile page
