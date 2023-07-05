from django.shortcuts import render
from .forms import RegistrationFrom

def register(request):
    form = RegistrationFrom()
    context = {
        'form':form
    }
    
    return render(request, 'accounts/register.html', context)


def login(request):
    
    return render(request, 'accounts/login.html')


def logout(request):
    
    return 