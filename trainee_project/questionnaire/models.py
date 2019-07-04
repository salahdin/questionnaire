from django.db import models
from datetime import date
from .validators import *

genderChoice = (
    ('Male', 'male'),
    ('Female', 'female')
)

YesorNo = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

LitracyChoice = (
    ('Literate', 'literate'),
    ('Illiterate', 'Illiterate'),
)


class Subject(models.Model):
    gender = models.CharField(
        verbose_name="Gender of the subject",
        choices=genderChoice,
        null=False,
        max_length=7
    )
    citizenship = models.CharField(
        verbose_name="is the subject a citizen of Botswana?",
        choices=YesorNo,
        null=False,
        blank=False,
        max_length=5
    )

    age = models.DateField(
        verbose_name="age of the subject",
        null=False,
        blank=False,
        validators=[validate_age_eligability]
    )

    literacy = models.CharField(
        verbose_name="is the subject literate or illiterate",
        choices=LitracyChoice,
        blank=False,
        null=False,
        max_length=20,
        
    )


    def is_minor(self):
        age = date.today() - self.age
        return age.year < 18