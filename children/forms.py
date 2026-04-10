from django import forms

from .models import Child


class ChildForm(forms.ModelForm):
    GENDER_CHOICES = [
        ("", "Select"),
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)

    class Meta:
        model = Child
        fields = ["name", "age", "gender", "notes"]
