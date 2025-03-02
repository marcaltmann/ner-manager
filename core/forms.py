from django import forms
from django.forms import ModelForm

from .models import InputFile


class UploadFileForm(forms.Form):
    file = forms.FileField(
        allow_empty_file=False,
        required=True,
        widget=forms.FileInput(attrs={"accept": "application/json"}),
    )


class InputFileForm(ModelForm):
    class Meta:
        model = InputFile
        fields = ["name"]
