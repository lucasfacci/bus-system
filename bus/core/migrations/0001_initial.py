# Generated by Django 5.0.1 on 2024-02-13 07:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('plate', models.CharField(max_length=7)),
                ('available_seats', models.IntegerField()),
                ('last_station', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
