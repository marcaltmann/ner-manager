# Generated by Django 5.0.6 on 2024-06-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_namedentity_timecode_namedentity_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='namedentity',
            name='timecode',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
