# Generated by Django 5.1.1 on 2024-11-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practice", "0007_practice_is_free"),
    ]

    operations = [
        migrations.AddField(
            model_name="practice",
            name="type",
            field=models.CharField(
                choices=[
                    ("gmat", "GMAT"),
                    ("sat", "SAT"),
                    ("gre", "GRE"),
                    ("other", "Other"),
                ],
                default="gmat",
                max_length=20,
            ),
        ),
    ]
