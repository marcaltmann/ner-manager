from django.db import models


class InputFile(models.Model):
    name = models.CharField(max_length=200)
    content = models.JSONField()

    def __str__(self):
        return self.name
