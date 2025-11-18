from django import forms

class CreateContactForm(forms.Form):
    full_name = forms.CharField(label="Name")
    specialty = forms.CharField(label="Specialty")
    city = forms.CharField(label="City")
    address = forms.CharField(label="Address")
    rating = forms.FloatField(required=False)
    fees = forms.IntegerField(required=False)
    phone = forms.CharField(label="Phone")
