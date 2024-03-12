from django.contrib import admin
from .models import Project, Participant, Element, SurveyResponse, Survey

# Register your models here.
admin.site.register(Project)

admin.site.register(Participant)

admin.site.register(Element)

admin.site.register(SurveyResponse)

admin.site.register(Survey)
