from django.contrib import admin
from .models import Project, Participant, Element, SurveyResponse, Survey, ElementResponse, Graph
from django.urls import path, reverse
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
    list_display = ('name', 'graph_link')  # Add graph_link to list_display

    def graph_link(self, obj):
        return '<a href="{}">View Graph</a>'.format(reverse('admin:graph', args=[obj.pk]))
    graph_link.allow_tags = True
    graph_link.short_description = 'Graph Link'


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
                    _, created = Element.objects.update_or_create(
                        ref_number=row[0],
                        category=row[1],
                        name=row[2],

                    )
                messages.success(request, "Your CSV file has been imported")
                return redirect("..")
        else:
            csv_form = CSVImportForm()
        context = self.admin_site.each_context(request)
        context['form'] = csv_form
        return render(request, "admin/csv_import.html", context)


# Register your models here.
admin.site.register(Project, ProjectAdmin)

admin.site.register(Participant)

admin.site.register(Element)

admin.site.register(ElementResponse)

admin.site.register(SurveyResponse)

admin.site.register(Survey)

admin.site.register(Graph)