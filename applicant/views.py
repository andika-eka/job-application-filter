from django.shortcuts import render
from django.shortcuts import redirect
from .models import Applicant
from .forms import ApplicantForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["applicants"] = Applicant.objects.all()

    return render(request, "index.html", context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'dashboard.html')


def apply(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ApplicantForm()
    return render(request, 'application_form.html', {
        'form': form})


def detail_view(request, id):
    context = {}
    context["applicants"] = Applicant.objects.get(id=id)
    return render(request, "index.html", context)
