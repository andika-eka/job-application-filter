from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'index.html')

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'dashboard.html')
