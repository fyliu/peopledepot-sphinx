# Generated by Django 4.0.7 on 2022-09-21 00:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringEvent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Start')),
                ('duration_in_min', models.IntegerField(blank=True, null=True)),
                ('video_conference_url', models.URLField(blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
