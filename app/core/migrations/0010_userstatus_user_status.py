# Generated by Django 4.0.8 on 2023-03-19 22:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'User statuses',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='users', to='core.userstatus'),
        ),
    ]