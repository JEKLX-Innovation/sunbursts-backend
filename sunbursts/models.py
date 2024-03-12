from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    name = models.CharField(max_length=255)
    goal = models.TextField()

class Participant(models.Model):
    project_name= models.ForeignKey(Project, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=255)
    participant_email = models.EmailField()
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False)

class Element(models.Model):
    name = models.CharField(max_length=255)

class Response(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    weighting_input = models.IntegerField(default=0)
    trend_input = models.IntegerField(default=0)
    readiness_input = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

