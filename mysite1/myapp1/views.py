from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact
from .form import CreateContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp1/home.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/success/')
    else:
        form = CreateContactForm()

    return render(request, 'myapp1/create_contact.html', {'form': form})

def update_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                setattr(contact, field, value)
            contact.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateContactForm(initial={
            'full_name': contact.full_name,
            'specialty': contact.specialty,
            'city': contact.city,
            'address': contact.address,
            'rating': contact.rating,
            'fees': contact.fees,
            'phone': contact.phone,
        })

    return render(request, 'myapp1/update_contact.html', {'form': form, 'id': id})

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return HttpResponseRedirect('/')

def success(request):
    return render(request, 'myapp1/success.html')
