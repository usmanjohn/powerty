# Generated by Django 5.1.1 on 2024-10-11 05:58

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=150)),
                ('topic_body', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('topic_category', models.CharField(choices=[('quant', 'Quant'), ('verbal', 'Verbal'), ('insight', 'Insight'), ('other', 'Other')], default='Topik', max_length=15)),
                ('topic_pub_date', models.DateTimeField(auto_now_add=True)),
                ('topic_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_auth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_body', models.TextField()),
                ('answer_pub_date', models.DateField(auto_now_add=True)),
                ('answer_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_auth', to=settings.AUTH_USER_MODEL)),
                ('topic_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='topics.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Upvoter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.SmallIntegerField(choices=[(1, 'upvote'), (-1, 'downvote')])),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='topics.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpvoterAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.SmallIntegerField(choices=[(1, 'upvote'), (-1, 'downvote')])),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='topics.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_topics', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_by_users', to='topics.topic')),
            ],
            options={
                'unique_together': {('user', 'topic')},
            },
        ),
    ]
