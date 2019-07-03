from .models import Subject
from django.test import TestCase
from .forms.form import SubjectForm
from datetime import date

class Setup_Class(TestCase):

    def setUp(self):
        self.user = Subject.objects.create(gender="Male", citizenship="Y", age=date.today(), literacy="Literate")

class Subject_Form_Test(TestCase):

    # Valid Form Data
    def test_SubjectForm_valid(self):
        form = SubjectForm(data={'gender': "Female", 'citizenship': "Y", 'age': date.today(), 'literacy': "Literate"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_SubjectForm_invalid(self):
        form = SubjectForm(data={'gender': "", 'citizenship': "", 'age': date.today(), 'literacy': ""})
        self.assertFalse(form.is_valid())