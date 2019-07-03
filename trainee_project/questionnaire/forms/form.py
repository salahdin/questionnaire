from django import forms
from ..models import Subject


class SubjectForm(forms.ModelForm):

    gender = forms.CharField(required=True, widget=forms.RadioSelect)

    citizenship = forms.CharField(required=True, widget=forms.RadioSelect)

    age = forms.DateField(required=True)

    literacy = forms.CharField(required=True, widget=forms.RadioSelect)


    class Meta:
        model = Subject
        fields = "__all__"
