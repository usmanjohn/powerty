from django.contrib import admin

from .models import Topic, Answer, SavedTopic
admin.site.register([Topic, Answer, SavedTopic])
