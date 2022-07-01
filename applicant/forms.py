from django import forms
from .models import Applicant
from django.forms import Form, CharField

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = (
            'name',
            'phone',
            'email',
            'document', )



class SearchForm(Form):
    search = CharField(required=False)