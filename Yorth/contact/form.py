from django import forms
from django.core.validators import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'contact-name', 'style': 'text-align: right'}),

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'id': 'contact-email', 'style': 'text-align: right'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-input', 'id': 'contact-phone', 'style': 'text-align: right', }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-input', 'id': 'contact-message', 'style': 'text-align: right'}))


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError(".نام را وارد کنید")

        elif len(name) < 3:
            raise ValidationError(".نام باید حداقل 3 کاراکتر داشته باشد")

        elif name.isdigit():
            raise ValidationError(".نام باید شامل حروف الفبا باشد")
        return name