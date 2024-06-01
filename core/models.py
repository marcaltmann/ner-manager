from django.db import models


class InputFile(models.Model):
    file = models.FileField(upload_to='files')
