from django import forms
from django.forms import ModelForm, inlineformset_factory

from .models import InputFile, NamedEntity


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


NamedEntityFormSet = inlineformset_factory(
    InputFile, NamedEntity, fields=["label", "name", "timecode", "segment"]
)
