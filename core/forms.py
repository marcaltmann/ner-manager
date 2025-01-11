from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        allow_empty_file=False,
        required=True,
        widget=forms.FileInput(attrs={"accept": "application/json"}),
    )
