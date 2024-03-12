# Generated by Django 4.1.5 on 2024-03-12 07:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(max_length=255)),
                ('participant_email', models.EmailField(max_length=254)),
                ('unique_link', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('goal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weighting_input', models.IntegerField(default=0)),
                ('trend_input', models.IntegerField(default=0)),
                ('readiness_input', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunbursts.element')),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sunbursts.participant')),
                ('project_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sunbursts.project')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sunbursts.project'),
        ),
        migrations.AddField(
            model_name='element',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sunbursts.project'),
        ),
    ]
