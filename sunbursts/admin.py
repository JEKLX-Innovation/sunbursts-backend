from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import CSVImportForm
import csv
import io

# # Register your models here.
# admin.site.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    change_list_template = "admin/project_change_list.html"

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
                csv_file = request.FILES['csv_file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string) 
                for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                    _, created = Project.objects.update_or_create(
                        name=row[0],
                        goal=row[1],
                    )
                messages.success(request, "Your CSV file has been imported")
                return redirect("..")
        else:
            csv_form = CSVImportForm()
        context = self.admin_site.each_context(request)
        context['form'] = csv_form
        return render(request, "admin/csv_import.html", context)

admin.site.register(Project, ProjectAdmin)