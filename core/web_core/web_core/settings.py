"""
Django settings for web_core project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from decouple import config
from pathlib import Path
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.

CORE_DIR = Path(__file__).resolve().parent.parent
CORE_ENV_FILE = os.path.join(CORE_DIR, 'core.env')
DB_DIR = os.path.normpath(os.path.join(CORE_DIR, 'core_package/databases'))
TP_DIR = os.path.normpath(os.path.join(CORE_DIR, 'core_package/templates'))
PK_DIR = os.path.normpath(os.path.join(CORE_DIR, 'core_package'))
load_dotenv(CORE_ENV_FILE)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if os.path.exists(CORE_ENV_FILE):
    SECRET_KEY = os.getenv["django_key"]
    print(f"SECRET_KEY: {SECRET_KEY}")
else:
    SECRET_KEY = config('SECRET_KEY', default='SECRET_KEY-django-insecure')
    print(f"SECRET_KEY: {SECRET_KEY}")
    print(" Create a core.env file with the SECRET_KEY variable")
    print(f"Directory: {CORE_ENV_FILE}")
                        
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
DEVEL = config('DEVEL', default=True, cast=bool)
PROD = config('PROD', default=False, cast=bool)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', config('SERVER', default='127.0.0.1')]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            TP_DIR,
        ],

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

WSGI_APPLICATION = 'web_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.normpath(os.path.join(DB_DIR, 'default/core_db.sqplite3')),
        'OPTIONS': { # useful when working with mariadb, mysql and others:
                #'read_default_file': os.path.normpath(os.path.join(DB_DIR, 'default/core_app.cnf')), # db configuration file
                #'name': os.path.normpath(os.path.join(DB_DIR, 'default/core_db.sqplite3')) # local db name
            },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.normpath(os.path.join(PK_DIR, 'static')),

]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
