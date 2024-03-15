"""
Registers models and admin classes.

This module registers models and admin classes with the Django admin site.

"""

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
from django.utils.html import format_html

class ParticipantAdmin(admin.ModelAdmin):
    """
    Admin class for Participant model.

    Specifies the display format for the Participant model in the admin interface.

    Attributes:
        list_display (tuple): Fields to display in the participant list.
    """

    list_display = ('participant_name', 'participant_email', 'survey_link')
    
    def survey_link(self, obj):
        """
        Generates a link to the participant's survey.

        Args:
            obj: Participant instance.

        Returns:
            str: HTML link to the participant's survey if available, otherwise "No link generated".
        """
        if obj.unique_link:
            url = obj.get_absolute_url()
            return format_html("<a href='{url}'>{url}</a>", url=url)
        return "No link generated"
    
    survey_link.short_description = 'Survey Link'

# Register models and admin classes
admin.site.register(Project, ProjectAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Element)
admin.site.register(ElementResponse)
admin.site.register(SurveyResponse)
admin.site.register(Survey)
admin.site.register(SunburstElement)