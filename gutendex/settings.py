

import environ
import os


# Import environment variables
env = environ.Env(
    ADMIN_EMAILS=(list, []),
    ADMIN_NAMES=(list, []),
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    MANAGER_EMAILS=(list, []),
    MANAGER_NAMES=(list, []),
)
environ.Env.read_env()
DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Other third-party apps
    'rest_framework',

    # Project apps
    'books',
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

ROOT_URLCONF = 'gutendex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gutendex/templates')],
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

WSGI_APPLICATION = 'gutendex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = env('STATIC_ROOT')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# User-uploaded files
MEDIA_ROOT = env('MEDIA_ROOT')
MEDIA_URL = '/media/'


# Users for error reporting
ADMIN_EMAILS = env('ADMIN_EMAILS')
ADMIN_NAMES = env('ADMIN_NAMES')
ADMIN_COUNT = len(ADMIN_EMAILS)
ADMINS = [
    (ADMIN_NAMES[i], ADMIN_EMAILS[i]) for i in range(ADMIN_COUNT)
]
MANAGER_EMAILS = env('MANAGER_EMAILS')
MANAGER_NAMES = env('MANAGER_NAMES')
MANAGER_COUNT = len(MANAGER_EMAILS)
MANAGERS = [
    (MANAGER_NAMES[i], MANAGER_EMAILS[i]) for i in range(MANAGER_COUNT)
]


# Email
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_ADDRESS = env('EMAIL_HOST_ADDRESS')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')


# Directory paths for catalog files and updater
BASE_CATALOG_DIR = os.path.join(BASE_DIR, 'catalog_files')
CATALOG_RDF_DIR = os.path.join(BASE_CATALOG_DIR, 'rdf')
CATALOG_INDEX_DIR = os.path.join(CATALOG_RDF_DIR, 'index.json')
CATALOG_LOG_DIR = os.path.join(BASE_CATALOG_DIR, 'log')
CATALOG_TEMP_DIR = os.path.join(BASE_CATALOG_DIR, 'tmp')


# Settings for Django REST Framework JSON API
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGE_SIZE': 32
}
