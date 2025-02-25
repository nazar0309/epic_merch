from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def contact_us(request):
    if request.method == "POST":
        print('Getting the POST request...')
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()

            # Get the cleaned data from the form
            cleaned_data = contact_form.cleaned_data
            user_message = cleaned_data.get('message')  # Assuming 'message' is a field in your form

            # Send the email to your inbox
            send_mail(
                'New Contact Us Message',  # Subject of the email
                user_message,  # The body of the email (user's message)
                cleaned_data.get('email'),  # The email of the user who submitted the form
                [settings.EMAIL_HOST_USER],  # Send to your email (set up in settings.py)
                fail_silently=False,  # Optionally set to True to ignore errors
            )

            # Show success message to the user
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your request has been submitted successfully. We will get back to you soon.'
            )

    else:
        contact_form = ContactForm()

    print('Rendering template...')
    return render(
        request,
        "contact_us/contact_us.html",
        {"contact_form": contact_form},
    )
