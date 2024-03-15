"""
Module containing views for CSV import in the admin panel.

Attributes:
    None

Classes:
    - ProjectAdmin: Admin class for managing CSV import in the admin panel.

Functions:
    None
"""
from django.contrib import admin, messages
from .forms import CSVImportForm
from django.urls import path
from django.shortcuts import render, redirect
import csv
import io
from .models import SunburstElement


class ProjectAdmin(admin.ModelAdmin):
    """
    Admin class for managing CSV import in the admin panel.
    """
    change_list_template = "admin/project_change_list.html"
    change_form_template = "admin/project_change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.import_csv, name="project_import_csv"),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_form = CSVImportForm(request.POST, request.FILES)
            if csv_form.is_valid():
                project = csv_form.cleaned_data['project']
                csv_file = request.FILES['csv_file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                    _, created = SunburstElement.objects.update_or_create(
                        project=project,
                        element_name=row[1],
                        point_score=row[10],
                        need_score=row[11],
                        score=row[12],
                        category=row[13],

                    )
                messages.success(request, "Your CSV file has been imported")
                return redirect("..")
        else:
            csv_form = CSVImportForm()
        context = self.admin_site.each_context(request)
        context['form'] = csv_form
        return render(request, "admin/csv_import.html", context)
