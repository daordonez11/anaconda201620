"""
Django settings for sonidos_libres project.

Generated by 'django-admin startproject' using Django 1.9.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4cv%k7bq5v*h8e0(e$*=c%&mqs7ix7d+2n_79ac=+l29zei$hs'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = [
    '*',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'rest_framework',
    'webpack_loader',
    'corsheaders',
    'storages',
    's3_folder_storage',
    #local apps
    'comercial_agent',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'sonidos_libres.urls'

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

WSGI_APPLICATION = 'sonidos_libres.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.environ.get('DJANGO_ENV') == 'production':

    DEBUG = True
    DATABASES = {'default': dj_database_url.config(default= os.environ.get('DATABASE_URL'))}
else:

    DEBUG = True
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'SonidosLibres',
                'HOST': 'localhost',
                'PORT': '5432'
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
if os.environ.get( 'DJANGO_ENV' ) == 'production':
    #ASW-S3 credentials
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    #AWS-S3 Settings
    DEFAULT_FILE_STORAGE = os.environ.get('DEFAULTFILES_STORAGE')
    DEFAULT_S3_PATH = 'media'
    MEDIA_URL = os.environ.get('MEDIA_URL')

    STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')
    STATIC_S3_PATH = 'static'
    STATIC_URL = os.environ.get('STATIC_URL')

    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    STATICFILES_DIRS = (
        # This lets Django's collectstatic store our bundles
        os.path.join(BASE_DIR, 'assets'),
        os.path.join(PROJECT_ROOT, 'static'),
    )

elif os.environ.get('DJANGO_ENV') == 'staging':
    # ASW-S3 credentials
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    # AWS-S3 Settings
    DEFAULT_FILE_STORAGE = os.environ.get('DEFAULTFILES_STORAGE')
    DEFAULT_S3_PATH = 'media'
    MEDIA_URL = os.environ.get('MEDIA_URL')

    #STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')
    STATIC_S3_PATH = 'static'
    STATIC_URL = '/static/'

    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    STATICFILES_DIRS = (
        # This lets Django's collectstatic store our bundles
        os.path.join(BASE_DIR, 'assets'),
        os.path.join(PROJECT_ROOT, 'static'),
    )

else:
    #Local Storage Settings
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

    STATICFILES_DIRS = (
        #This lets Django's collectstatic store our bundles
        os.path.join(BASE_DIR, 'assets'),
        os.path.join(PROJECT_ROOT, 'static'),
    )


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
