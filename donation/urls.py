from django.urls import path
from . import views

app_name = 'donation'
urlpatterns = [
    path('', views.DonationView.as_view(), name='donation'),

]
