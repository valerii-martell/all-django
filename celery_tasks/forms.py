from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class TotalForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(50000)
        ]
    )