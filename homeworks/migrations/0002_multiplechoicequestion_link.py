# Generated by Django 5.1.1 on 2024-10-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='link',
            field=models.URLField(blank=True, default='https://www.youtube.com/', null=True),
        ),
    ]
