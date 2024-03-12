from django.db import transaction
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Sunburst, Participant, Element, Response
from .permissions import IsOwnerOrReadOnly
from .serializers import SunburstSerializer
from .forms import SurveyForm

class SunburstListView(ListCreateAPIView):
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer


class SunburstDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer


def survey_form(request, unique_link):
    try:
        participant = Participant.objects.get(unique_link=unique_link)
    except Participant.DoesNotExist:
        raise Http404("Participant does not exist")

    # Example of filtering elements; adjust the filter as per your requirements.
    elements = Element.objects.filter(is_active=True)  # Assuming there's an 'is_active' field.

    if request.method == 'POST':
        form = SurveyForm(request.POST, elements=elements)
        if form.is_valid():
            with transaction.atomic():
                for element in form.cleaned_data['selected_elements']:
                    response = Response(
                        participant=participant,
                        element=element,
                        points=form.cleaned_data['points']
                    )
                    response.save()
            return redirect('survey:thank_you')
    else:
        form = SurveyForm(elements=elements)

    return render(request, 'sunbursts/survey_form.html', {'form': form})

def thank_you(request):
    return render(request, 'survey/thank_you.html')




# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from .models import Sunburst
# from .permissions import IsOwnerOrReadOnly
# from .serializers import SunburstSerializer
# from .forms import SurveyForm
# from .models import Project, Participant, Element, Response
# from django.shortcuts import render, redirect

# class SunburstListView(ListCreateAPIView):
#     queryset = Sunburst.objects.all()
#     serializer_class = SunburstSerializer


# class SunburstDetailView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Sunburst.objects.all()
#     serializer_class = SunburstSerializer


# def survey_form(request, unique_link):
#     participant = Participant.objects.get(unique_link=unique_link)
#     elements = Element.objects.all()

#     if request.method == 'POST':
#         form = SurveyForm(request.POST, elements=elements)
#         if form.is_valid():
#             for element in form.cleaned_data['selected_elements']:
#                 response = Response(participant=participant, element=element, points=form.cleaned_data['points'])
#                 response.save()
#             return redirect('survey:thank_you')
#     else:
#         form = SurveyForm(elements=elements)

#     return render(request, 'sunbursts/survey_form.html', {'form': form})

# def thank_you(request):
#     return render(request, 'survey/thank_you.html')

