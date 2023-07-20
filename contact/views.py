from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Get the contact form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            massage = form.cleaned_data['massage']

            # Prepare the email content
            subject = f"Contacted us from {name}"
            body = f"Name: {name}\nEmail: {email}\nAddress: {address}\nMessage: {massage}"

            send_mail(subject, body, 'web.developer6282@gmail.com', ['web.developer6282@gmail.com'], fail_silently=False)

            messages.success(request, "Thanks for contacting us. We will reach out to you soon!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')
