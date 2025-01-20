from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    if request.method == "POST":
        print('Getting the POST request...')
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your request has been submitted successfully.'
                'We will get back to you soon.'
            )

    else:
        contact_form = ContactForm()

    print('Rendering template...')
    return render(
        request,
        "contact_us/contact_us.html",
        {"contact_form": contact_form},
    )
