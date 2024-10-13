# Generated by Django 5.1.1 on 2024-10-12 16:34

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0007_alter_testattempt_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='category',
            field=models.CharField(choices=[('quant', 'Quant'), ('verbal', 'Verbal'), ('insight', 'Insight'), ('all', 'All')], default='quant', max_length=20),
        ),
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage(), upload_to='question_images/'),
        ),
    ]
