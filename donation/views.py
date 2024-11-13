from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.

class DonationView(TemplateView):
    template_name = "donation/donation.html"
