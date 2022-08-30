from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class GenerateRandomUserForm(forms.Form):
    print("form")
    total = forms.IntegerField(
        validators=[
            MinValueValidator(1, 'The number of users must be greater than 0'),
            MaxValueValidator(50, 'The number of users must be less than 50')
        ]
    )
