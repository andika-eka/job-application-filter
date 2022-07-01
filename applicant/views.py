import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from regex import R
from .models import Applicant
from .forms import ApplicantForm
from .forms import SearchForm
from django.contrib.auth.decorators import user_passes_test
import pdfplumber
import pysolr 
from django.db.models import Case, When


# Create your views here.

def give_and(text):
    text = text.split() 
    out = 'cv_text:"'+ text[0] + '" ' 
    for word in text[1:]:
        out += 'AND cv_text:"'+ word + '" ' 
    return out
        
def give_or(text):
    text = text.split() 
    out = 'cv_text:"'+ text[0] + '" ' 
    for word in text[1:]:
        out += 'OR cv_text:"'+ word + '" ' 
    return out
        

@user_passes_test(lambda u: u.is_superuser)
def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
    solr = pysolr.Solr("http://localhost:8983/solr/cv_filter/")

    query = str(query)
    if len(query.split()) > 1:
        solr_query = give_and(query)
        results = solr.search(solr_query, **{
            'rows': 500,
            'sort': "score desc"
        })
        # id_and = {result['id'] for result in results}
        ids = [result['id'] for result in results]
        
        # solr_query = give_or(query)
        # results = solr.search(solr_query, **{
        #     'rows': 500,
        # })
        # id_or = {result['id'] for result in results}

        # ids = id_and.union(id_or)

    else :
        solr_query = 'cv_text:"'+ query + '" ' 

        results = solr.search(solr_query, **{
            'rows': 500,
            'sort': "score desc"
        })
        ids = [result['id'] for result in results]
    
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    applicants = Applicant.objects.filter(id__in=ids).order_by(preserved)
    context = {}
    context["search_form"] = ApplicantForm()
    context["num"] = len(applicants)
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
    context = {}


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



