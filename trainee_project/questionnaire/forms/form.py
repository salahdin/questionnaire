from django import forms
from ..models import Subject

class DateInput(forms.DateInput):
    input_type = 'date'


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            'age': DateInput(),
        }
        