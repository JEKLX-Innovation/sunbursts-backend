from django import forms
from .models import Element

class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        elements = kwargs.pop('elements')
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['selected_elements'] = forms.ModelMultipleChoiceField(
            queryset=elements,
            widget=forms.CheckboxSelectMultiple,
            required=True
        )
        self.fields['points'] = forms.IntegerField()

