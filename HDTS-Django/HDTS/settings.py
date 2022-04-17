"""
Django settings for HDTS project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6oii^+w*=n88*uh$866f19yln6!4i@eutt*astet*$bwe3&o6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#CHANGE LATER TO USE .ENV
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # our apps
    'Inventory.apps.InventoryConfig',
    'accounts.apps.AccountsConfig',
    'request.apps.RequestConfig',
    'crispy_forms',

    # django apps
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

ROOT_URLCONF = 'HDTS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'HDTS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# #CHANGE LATER TO USE .ENV VARIABLES
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'hdts',
#         'CLIENT': {
#             'username': 'team7',
#             'password': 'team7',
#             'host': 'hdts.azemend.com',
#             'port': 4444,
#         }

#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK="bootstrap4"

LOGIN_REDIRECT_URL="/login.html"
LOGOUT_REDIRECT_URL="/"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'filters': {
       'filter_info_level': {
           '()': 'HDTS.log_middleware.FilterLevels',
           'filter_levels' : [
               "INFO"
           ]
       },
       'filter_error_level': {
           '()': 'HDTS.log_middleware.FilterLevels',
           'filter_levels' : [
               "ERROR"
           ]
       },
       'filter_warning_level': {
           '()': 'HDTS.log_middleware.FilterLevels',
           'filter_levels' : [
               "WARNING"
           ]
       }
   },
   'formatters': {
       'info-formatter': {
           'format': '%(levelname)s : %(message)s - [in %(pathname)s:%(lineno)d]'
       },
       'error-formatter': {
           'format': '%(levelname)s : %(asctime)s {%(module)s} [%(funcName)s] %(message)s- [in %(pathname)s:%(lineno)d]',
           'datefmt': '%Y-%m-%d %H:%M'
       },
       'short': {
           'format': '%(levelname)s : %(message)s'
       }
   },
   'handlers': {
       'customHandler_1': {
           'formatter': 'info-formatter',
           'class': 'HDTS.log_middleware.DatabaseLoggingHandler',
           'database': 'HDTS',
           'collection': 'logs',
           'filters': ['filter_info_level'],
       },
       'customHandler_2': {
           'formatter': 'error-formatter',
           'class': 'HDTS.log_middleware.DatabaseLoggingHandler',
           'database': 'HDTS',
           'collection': 'logs',
           'filters': ['filter_error_level'],
       },
       'customHandler_3': {
           'formatter': 'short',
           'class': 'logging.StreamHandler',
           'filters': ['filter_warning_level'],
       },
   },
   'loggers': {
       'customLogger': {
           'handlers': [
               'customHandler_1',
               'customHandler_2',
               'customHandler_3'
           ],
           'level': 'DEBUG',
       },
   },
}

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.AllowAny',
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
  ),
  'EXCEPTION_HANDLER': 'HDTS.exception_handler.handle_exception'
}