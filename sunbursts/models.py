from typing import Any
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class Project(models.Model):
    name = models.CharField(max_length=255)
    goal = models.TextField()
    def __str__(self) -> Any:
        return self.name


class Participant(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    participant_name = models.CharField(max_length=255)
    participant_email = models.EmailField()
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self) -> Any:
        return self.participant_name


class Survey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    # selected_elements = models.ManyToManyField(Element)
    user_selections_max = models.IntegerField(default=10)
    weighting_max = models.IntegerField(default=20)
    readiness_score_max = models.IntegerField(default=10)
    def __str__(self) -> Any:
        return self.project.name


class Element(models.Model):
    # project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self) -> Any:
        return self.name


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True)
    # responses = models.ForeignKey(Response, on_delete=models.CASCADE, null=True, blank=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> Any:
        return self.survey.project.name


class ElementResponse(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE, null=True, blank=True)
    weighting_input = models.IntegerField(default=0)
    trend_input = models.IntegerField(default=0)
    readiness_input = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    def __str__(self) -> Any:
        return self.element.name
