# Generated by Django 5.1.1 on 2024-10-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practice", "0006_alter_practice_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="practice",
            name="is_free",
            field=models.BooleanField(default=False),
        ),
    ]