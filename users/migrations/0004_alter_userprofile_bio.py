# Generated by Django 5.1.1 on 2024-10-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='I did not write a bio yet', max_length=2000),
        ),
    ]
