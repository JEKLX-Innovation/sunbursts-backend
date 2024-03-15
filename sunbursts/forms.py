"""
Defines a form for importing CSV files associated with projects in Django.

This module provides the CSVImportForm class, which is a Django form used for importing CSV files
associated with projects. It includes fields for uploading a CSV file and selecting a project.

"""

from django import forms
from .models import Project

class CSVImportForm(forms.Form):
    """
    Form for importing CSV files associated with projects.

    Inherits from Django's Form class.

    Attributes:
        csv_file (FileField): Field for uploading a CSV file.
        project (ModelChoiceField): Field for selecting a project.
    """
    csv_file = forms.FileField()
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Select a Project")