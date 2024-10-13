from django.contrib import admin
from .models import Test, MultipleChoiceQuestion
admin.site.register([Test, MultipleChoiceQuestion])
