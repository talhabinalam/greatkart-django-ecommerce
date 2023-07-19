from django.shortcuts import render
from .models import ContactUs
from .forms import ContactUsForm


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactUsForm()
        
    return render(request, 'contactus.html', {'form':form})
