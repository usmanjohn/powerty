# Generated by Django 5.1.1 on 2024-11-06 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homeworks", "0014_test_fa_icon_test_icon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test",
            name="fa_icon",
        ),
        migrations.RemoveField(
            model_name="test",
            name="icon",
        ),
    ]