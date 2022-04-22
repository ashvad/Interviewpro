from django import forms
from hello.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control","placeholder":"Name"}),
            "Date": forms.DateInput(attrs={"class": "form-control","placeholder":"Date"}),
            "Email": forms.EmailInput(attrs={"class": "form-control","placeholder":"Email"}),
            "income": forms.NumberInput(attrs={"class": "form-control","placeholder":"income"}),
            "Ip_address": forms.TextInput(attrs={"class": "form-control","placeholder":"Ip_address"})
        }
