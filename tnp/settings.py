"""
Django settings for tnp project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7829a42e-0b4c-4e22-b5df-49d02317658c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if os.name == 'nt':
    DEBUG = True

ALLOWED_HOSTS = ['tnp-env.mrbpzegphg.us-east-1.elasticbeanstalk.com','localhost','tnp.nsutonline.in']


# Application definition

INSTALLED_APPS = [
    # Add your apps here to enable them
    'student',
    'management',
    'django_cleanup',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    # 'webpush',
    
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tnp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tnp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.name != 'nt':
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'tnpdb',
            'USER': 'tnpdb',
            'PASSWORD': '1234Admin',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'tnpdb',
            'USER': 'tnpdb',
            'PASSWORD': '1234Admin',
            'HOST': 'localhost',
            'PORT': '9274',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'

#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
if os.name == 'nt':
    MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))
    MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

DEFAULT_FROM_EMAIL = 'noreply@tnp.nsutonline.in'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST='smtp.sendgrid.net'
EMAIL_HOST_USER='apikey'
EMAIL_HOST_PASSWORD = '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'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

#######################################################################################
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_ACCESS_KEY_ID = 'AKIAQ24SWITU5SEVXMBN'
AWS_SES_SECRET_ACCESS_KEY = '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'

#######################################################################################

DATE_INPUT_FORMAT = '%m/%d/%Y'

LOGIN_URL = 'student:s_login'
LOGOUT_REDIRECT_URL = 'student:s_login'
LOGIN_REDIRECT_URL='student:s_profile'

CONTENT_TYPES = ['xlsx', 'xlsx','vnd.openxmlformats-officedocument.spreadsheetml.sheet']
CONTENT_TYPES_PDF = ['pdf', 'pdf']
MAX_UPLOAD_SIZE = 1048576

MESSAGE_TAGS = {
    messages.ERROR: 'red',
    messages.SUCCESS:'green',
    messages.WARNING:'yellow',
    messages.INFO:'purple darken-3'
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AWS_ACCESS_KEY_ID = 'AKIAQ24SWITU54I2HEU4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'tnpnsutstaticbucket'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
AWS_DEFAULT_ACL = 'public-read'

DEFAULT_FILE_STORAGE = 'tnp.storage_backends.MediaStorage'

if os.name!='nt':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*'
}

# WEBPUSH_SETTINGS = {
#     "VAPID_PUBLIC_KEY": "BNhdj8k16qvv97fZ-CSw4m8o78GwDKUvOrLQe90HUnPmM84Dkuqdwb8PgsJ4Qfa473saQDCCuAvj2OMKhDep1NU",
#     "VAPID_PRIVATE_KEY":"E6fq8txi3OZQsj-vGGnkd8PITbFFxyPfSuVqHl4rSNw",
#     "VAPID_ADMIN_EMAIL": "no-reply@tnp.nsutonline.in"
# }
#