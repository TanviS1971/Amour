from django import forms

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal'),
)

class AddressForm(forms.Form):
    street_address = forms.CharField(required=False)
    apartment_address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    pin = forms.CharField(required=False)
    save_info = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)