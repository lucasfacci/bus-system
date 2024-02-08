# Generated by Django 5.0.1 on 2024-02-08 01:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_travel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Station',
                'verbose_name_plural': 'Stations',
                'ordering': ['id'],
            },
        ),
    ]
