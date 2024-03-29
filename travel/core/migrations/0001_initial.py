# Generated by Django 5.0.1 on 2024-01-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('destiny', models.CharField(max_length=255)),
                ('departure', models.TimeField()),
                ('arrival', models.TimeField()),
                ('forecast', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
