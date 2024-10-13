# general/management/commands/print_aws_settings.py

from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Print AWS settings to verify configuration'

    def handle(self, *args, **kwargs):
        aws_settings = {
            'AWS_ACCESS_KEY_ID': settings.AWS_ACCESS_KEY_ID,
            'AWS_SECRET_ACCESS_KEY': settings.AWS_SECRET_ACCESS_KEY,
            'AWS_STORAGE_BUCKET_NAME': settings.AWS_STORAGE_BUCKET_NAME,
            'AWS_S3_REGION_NAME': settings.AWS_S3_REGION_NAME,
            'AWS_S3_CUSTOM_DOMAIN': settings.AWS_S3_CUSTOM_DOMAIN,
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATICFILES_STORAGE': settings.STATICFILES_STORAGE,
            'DEFAULT_FILE_STORAGE': settings.DEFAULT_FILE_STORAGE,
        }

        for key, value in aws_settings.items():
            self.stdout.write(f"{key}: {value}")
