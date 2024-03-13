# Generated by Django 5.0.1 on 2024-01-17 09:55

import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="city",
            field=models.CharField(default="NY", max_length=60),
        ),
        migrations.AddField(
            model_name="location",
            name="state",
            field=localflavor.us.models.USStateField(default="NY", max_length=2),
        ),
        migrations.AddField(
            model_name="location",
            name="zipcode",
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
    ]
