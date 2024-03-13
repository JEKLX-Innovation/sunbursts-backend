# from django.db import transaction
# from django.http import Http404
# from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Project, Survey, Element
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer, SurveySerializer, ElementSerializer

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SurveyCreateView(RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class ElementListView(ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ElementDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
