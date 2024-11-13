from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('contacts', views.contacts_view, name='contact'),
]
