# Generated by Django 5.1.1 on 2024-10-08 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0005_testattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='test_attempt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homeworks.testattempt'),
        ),
    ]
