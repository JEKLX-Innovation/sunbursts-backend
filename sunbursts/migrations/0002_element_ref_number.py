# Generated by Django 4.1.5 on 2024-03-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunbursts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='ref_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
