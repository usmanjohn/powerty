# Generated by Django 5.1.1 on 2024-12-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0003_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutorial",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]