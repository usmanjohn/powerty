from django.contrib import admin
from .models import Test, MultipleChoiceQuestion, TestAttempt, UserAnswer
admin.site.register([Test, MultipleChoiceQuestion, TestAttempt, UserAnswer])
