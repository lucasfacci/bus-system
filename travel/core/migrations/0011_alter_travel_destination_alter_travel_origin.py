# Generated by Django 5.0.1 on 2024-02-08 01:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_type_travel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='core.station'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='core.station'),
        ),
    ]