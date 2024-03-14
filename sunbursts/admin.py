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
from .models import Project


# Register your models here.
admin.site.register(Project, ProjectAdmin)

admin.site.register(Participant)

admin.site.register(Element)

admin.site.register(ElementResponse)

admin.site.register(SurveyResponse)

admin.site.register(Survey)

admin.site.register(SunburstElement)
