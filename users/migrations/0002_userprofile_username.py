# Generated by Django 5.1.1 on 2024-10-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='alfabret', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
