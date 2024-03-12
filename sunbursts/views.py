# from django.db import transaction
# from django.http import Http404
# from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Project, Survey
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer, SurveySerializer

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SurveyCreateView(ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

# def survey_form(request, unique_link):
#     try:
#         participant = Participant.objects.get(unique_link=unique_link)
#     except Participant.DoesNotExist:
#         raise Http404("Participant does not exist")

#     # Example of filtering elements; adjust the filter as per your requirements.
#     elements = Element.objects.filter(is_active=True)  # Assuming there's an 'is_active' field.

#     if request.method == 'POST':
#         form = SurveyForm(request.POST, elements=elements)
#         if form.is_valid():
#             with transaction.atomic():
#                 for element in form.cleaned_data['selected_elements']:
#                     response = Response(
#                         participant=participant,
#                         element=element,
#                         points=form.cleaned_data['points']
#                     )
#                     response.save()
#             return redirect('survey:thank_you')
#     else:
#         form = SurveyForm(elements=elements)

#     return render(request, 'sunbursts/survey_form.html', {'form': form})

# def thank_you(request):
#     return render(request, 'survey/thank_you.html')

