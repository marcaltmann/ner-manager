# Generated by Django 5.0.6 on 2024-06-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_namedentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputfile',
            name='content',
        ),
    ]