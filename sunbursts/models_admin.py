from django.contrib import admin, messages
from .forms import CSVImportForm
from django.urls import path
from django.shortcuts import render, redirect
import csv
import io
from .models import SunburstElement, Participant


class ProjectAdmin(admin.ModelAdmin):
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
                # participant = csv_form.cleaned_data['participant']
                csv_file = request.FILES['csv_file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                reader = csv.DictReader(io_string)
                for row in reader:
                    print(row)
                    if not row.get('Element Name') or not row.get('Point Score') or not row.get('Need Score') or not row.get('Score') or not row.get('Category') or not row.get('Participant Name'):
                        print("Skipping row due to missing data")
                        continue

                    _, created = SunburstElement.objects.update_or_create(
                        project=project,
                        element_name=row['Element Name'],
                        point_score=row['Point Score'],
                        need_score=row['Need Score'],
                        score=row['Score'],
                        category=row['Category'],
                    )
                    _, created = Participant.objects.update_or_create(
                        participant_name=row['Participant Name'],
                        participant_email=row['Participant Email']
                    )

                messages.success(request, "Your CSV file has been imported")
                return redirect("..")
        else:
            csv_form = CSVImportForm()
        context = self.admin_site.each_context(request)
        context['form'] = csv_form
        return render(request, "admin/csv_import.html", context)
