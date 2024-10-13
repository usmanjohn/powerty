# settings.py

import os
from pathlib import Path


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
import dj_database_url
# Load environment variables

# Secret key and debug (ensure SECRET_KEY is kept secret in production)
SECRET_KEY = os.environ.get('SECRET_KEY', default='your-default-secret-key')  # Replace or manage securely
DEBUG = False

ALLOWED_HOSTS = ["*"]  # Update as needed for production

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'users',
    'tutorials',
    'topics',
    'homeworks',
    
    'general',
    'practice',
    'storages',
    'widget_tweaks',
    'django.contrib.humanize',
    'django_ckeditor_5',
    "crispy_forms",
    "crispy_bootstrap5",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # Removed to prevent conflicts with S3
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL Configuration
ROOT_URLCONF = "gmat.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = "gmat.wsgi.application"

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3'
    )
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'users.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# AWS Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = None  # Recommended to set to None to use bucket ACLs
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_VERIFY = True

# Static files configuration
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'gmat.storages_backends.StaticStorage'

# Media files configuration
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'gmat.storages_backends.MediaStorage'

# Authentication settings
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Crispy Forms Settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = "media/"
CKEDITOR_5_CONFIGS = {
    # Your CKEditor configurations
}

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'level':'INFO',
        },
        'storages': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Set to DEBUG to see detailed logs
        },
    },
}

customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Red'},
    {'color': 'hsl(340, 82%, 52%)', 'label': 'Pink'},
    {'color': 'hsl(291, 64%, 42%)', 'label': 'Purple'},
    {'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple'},
    {'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo'},
    {'color': 'hsl(207, 90%, 54%)', 'label': 'Blue'},
]
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'],
        'width': '100%',
    },
    'extends': {
        'width': '100%',
        'blockToolbar': ['paragraph', 'heading1', 'heading2', 'heading3', '|', 'bulletedList', 'numberedList', '|', 'blockQuote'],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough', 'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage', 'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|', 'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat', 'insertTable'],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft', 'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side'],
            'styles': ['full', 'side', 'alignLeft', 'alignRight', 'alignCenter'],
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells', 'tableProperties', 'tableCellProperties'],
            'tableProperties': {'borderColors': customColorPalette, 'backgroundColors': customColorPalette},
            'tableCellProperties': {'borderColors': customColorPalette, 'backgroundColors': customColorPalette},
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
            ],
        },
        'width': 'auto',
    },
    'list': {
        'properties': {'styles': 'true', 'startIndex': 'true', 'reversed': 'true'},
        'width': 'auto',
    },
}
