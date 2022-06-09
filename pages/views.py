from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def apply(request):
    return render(request, 'application_form.html')