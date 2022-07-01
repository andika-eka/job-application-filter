from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Applicant
from .forms import ApplicantForm
from .forms import SearchForm
from django.contrib.auth.decorators import user_passes_test
import pdfplumber
import pysolr 

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
    solr = pysolr.Solr("http://localhost:8983/solr/cv_filter/")
    results = solr.search('cv_text:"{0}"'.format(query))
    ids = [result['id'] for result in results]
    applicants = Applicant.objects.filter(id__in=ids)
    context = {}
    context["search_form"] = ApplicantForm()
    context["query"] = query
    context["applicants"] = applicants
    return render(request, "search.html", context)

def get_txt(path):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    return text

@user_passes_test(lambda u: u.is_superuser)
def indexing(request):
    applicants = Applicant.objects.all()
    solr = pysolr.Solr("http://localhost:8983/solr/cv_filter/")
    solr.delete("q=*.*")
    solr.commit()
    for applicant in applicants:
        json = {
            'id' : applicant.id,
            'email' : applicant.email,
            'cv_text' : get_txt('./media/'+ str(applicant.document))
        }
        solr.add(json)
        solr.commit()
    solr.optimize()
    # print("test:")
    return HttpResponse("OK")




@user_passes_test(lambda u: u.is_superuser)
def index(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["applicants"] = Applicant.objects.all()
    context["search_form"] = SearchForm()

    return render(request, "index.html", context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    context = {}
    context["search_form"] = SearchForm()
    return render(request, 'dashboard.html',context)


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



