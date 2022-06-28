from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Applicant
from .forms import ApplicantForm
from django.contrib.auth.decorators import user_passes_test
import pdfplumber

# Create your views here.


def get_txt(path):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    
    return text

@user_passes_test(lambda u: u.is_superuser)
def indexing(request):
    applicants = Applicant.objects.all()
    # print("test:")
    data = { 'message': "data indexed" }
    return JsonResponse(data)




@user_passes_test(lambda u: u.is_superuser)
def index(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    print("test")

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



