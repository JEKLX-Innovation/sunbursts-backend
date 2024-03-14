from django import forms
from .models import Project

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select a Project")
