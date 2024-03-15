from django.contrib import admin
from .models import (
    Project,
    Participant,
    Element,
    SurveyResponse,
    Survey,
    ElementResponse,
    SunburstElement)
from .models_admin import ProjectAdmin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import format_html

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'participant_email', 'survey_link')
    
    def survey_link(self, obj):
        if obj.unique_link:
            url = obj.get_absolute_url()
            return format_html("<a href='{url}'>{url}</a>", url=url)
        return "No link generated"
    survey_link.short_description = 'Survey Link'

# Register your models here.
admin.site.register(Project, ProjectAdmin)

admin.site.register(Participant, ParticipantAdmin)

admin.site.register(Element)

admin.site.register(ElementResponse)

admin.site.register(SurveyResponse)

admin.site.register(Survey)

admin.site.register(SunburstElement)
