"""
Django settings for all_django project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import importlib
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*#k32tqcb8)^&e-y8wy^!tlewwd7qiruwcs&owt#famyp$zfpb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'grappelli',
    # 'django_admin_index',
    # 'custom_admin.apps.SuitConfig',
    'custom_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'durationwidget',
    'phone_field',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'django_celery_results',
    'index',
    'smoke',
    'routing',
    'views',
    'templates',
    'models',
    'forms',
    'orm',
    'authentication',
    'ajax',
    'api',
    'security',
    'custom_user',
    # 'custom_admin',
    'frontend',
    'emails',
    'graphql_api',
    'celery_redis'
]

# Solve Django 4 issue with deprecated functions
import django
from django.utils.encoding import force_str
from django.utils.translation import gettext, gettext_lazy
django.utils.encoding.force_text = force_str
django.utils.translation.ugettext, django.utils.translation.ugettext_lazy = gettext, gettext_lazy
# Solve graphql_jwt issue with deprecated in Django 4 providing_args parameter in dispatch.Signal constructor
# import sys
# from graphql_jwt.signals import
# del sys.modules['graphql_jwt.signals']
# sys.modules['graphql_jwt.signals'] = __import__('signals')
# import graphql_jwt.signals
# module = importlib.import_module(graphql_jwt.signals)
# graphql_jwt.signals.token_issued = django.dispatch.Signal(['request', 'user'])
# graphql_jwt.signals.token_refreshed = django.dispatch.Signal(['request', 'user'])
# import graphql_jwt.signals
# graphql_jwt.signals.__dict__['token_issued'] = django.dispatch.Signal(['request', 'user'])
# graphql_jwt.signals.__dict__['token_refreshed'] = django.dispatch.Signal(['request', 'user'])


# AUTH_USER_MODEL = 'graphql_api.ApiClient'

AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend'
]

GRAPHENE = {
    'SCHEMA': 'schema.schema',
    # 'MIDDLEWARE': [
    #     'graphql_jwt.middleware.JSONWebTokenMiddleware'
    # ]
}

GRAPHQL_JWT = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',)
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'all_django.urls'

SESSION_COOKIE_AGE = 3600

# Redis
# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = 'redis'

# RabbitMQ
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Amsterdam'

# CELERY_BEAT_SCHEDULE = {
#     "weather": {
#         "task": "celery_redis.tasks.fetch_weather",
#         "schedule": 20.0,
#         'session_cleanup': nightly_schedule
#     },
# }

# celery -A all_django worker -l DEBUG/INFO
# from celery_redis.tasks import fibon
# task = fibon.delay(100000)
# task.get()
# celery -A all_django events
# pip install flower
# celery flower (localhost:5555)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django_admin_index.context_processors.dashboard',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates/templates'],
        'APP_DIRS': True,
        # 'OPTIONS': {
        #     'environment': 'templates.jinja2.environment',
        # }
        # 'OPTIONS': {
        #     'context_processors': [
        #         'django.template.context_processors.debug',
        #         'django.template.context_processors.request',
        #         'django.contrib.auth.context_processors.auth',
        #         'django.contrib.messages.context_processors.messages',
        #     ],
        # },
    },
]

WSGI_APPLICATION = 'all_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # add STATIC_ROOT to DIRS
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# GMAIL CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = f"All-Django Team <{os.environ.get('EMAIL_HOST_USER')}>"  # 'TestSite Team <noreply@example.com>'

# AWS CONFIG
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'email-smtp.us-east-2.amazonaws.com'
# EMAIL_HOST_USER = 'AKIA5ZT43BP5LNAO3QTY'
# EMAIL_HOST_PASSWORD = 'BFzrmpzbO6qEQc3yP8hcSYD5f2f/E8R/MBLxk6YEcQq6'


# MAILCHIMP CONFIG
MAILCHIMP_API_KEY = "c68cc4d896d760c468d62de88ab0c940-us7"
MAILCHIMP_DATA_CENTER = "us7"
MAILCHIMP_EMAIL_LIST_ID = "4dd3fadb19"
