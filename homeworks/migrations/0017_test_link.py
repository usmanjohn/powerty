# Generated by Django 5.1.1 on 2024-11-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeworks", "0016_test_order_test_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="link",
            field=models.URLField(
                blank=True,
                default="youtube.com/channel/UCv2shQIaFCsfUL29YL9uxIQ",
                null=True,
            ),
        ),
    ]