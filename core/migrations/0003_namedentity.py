# Generated by Django 5.0.6 on 2024-06-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_inputfile_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="NamedEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("timecode", models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
