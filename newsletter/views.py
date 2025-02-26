from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import NewsletterSubscriber
from .forms import NewsletterForm


def subscribe_newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email is already in the newsletter subscriber database
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                form.save()

                # Send welcome email
                subject = "Welcome to our Newsletter!"
                profile_url = request.build_absolute_uri('/profile/')  # Assuming the user profile URL is '/profile/'
                message = f"Thank you for subscribing to our newsletter, {email}.\n\n" \
                          f"You can view your profile here: {profile_url}"

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(request, "You have successfully subscribed!")
            else:
                messages.warning(request, "You are already subscribed.")
        else:
            messages.error(request, "Invalid email address.")
    
    return redirect('home')

