from django.shortcuts import render, redirect
from hello.forms import AddressForm
from django.views.generic import View
from hello.models import Address


class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, "add_address.html", {"form": form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("listaddress")
        else:
            return render(request, "add_address.html", {"form": form})


class Addresslist(View):
    def get(self, request):
        print("here")
        qs = Address.objects.all()
        return render(request, "address_list.html", {"address": qs})


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        qs = Address.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("listaddress")
