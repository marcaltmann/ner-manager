from django.db import models


class InputFile(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NamedEntity(models.Model):
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    timecode = models.DecimalField(max_digits=10, decimal_places=3,
                                   null=False, blank=False)
    segment = models.TextField(null=False, blank=False)
    input_file = models.ForeignKey(InputFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
