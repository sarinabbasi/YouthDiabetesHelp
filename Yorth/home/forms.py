from django import forms
from .models import SubscribeModel  # Make sure to import your model here

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SubscribeModel
        fields = []  # Add the appropriate fields if needed
