from django.shortcuts import render
from . import models
from .form import ContactForm


from django.shortcuts import render
from .models import BannerImage, Email, Address, Number
from .form import ContactForm
from django.http import JsonResponse

def contacts_view(request):
    success_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the form is valid, process the data and save it to the database
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            models.ContactModel.objects.create(name=name, email=email, phone=phone, message=message)

            success_message = "Form submitted successfully"  # Set the success message

    else:
        form = ContactForm()

    banner = BannerImage.objects.last()
    email_info = Email.objects.all()
    address_info = Address.objects.last()
    number_info = Number.objects.all()

    context = {
        'contact_data': {
            'banner': banner,
            'email': email_info,
            'address': address_info,
            'number': number_info,
        },
        'form': form,
        'success_message': success_message,  # Pass the success message to the template
    }

    return render(request, "contact/contacts.html", context)
