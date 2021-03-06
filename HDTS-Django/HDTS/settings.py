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
#SECRET_KEY = 'django-insecure-6oii^+w*=n88*uh$866f19yln6!4i@eutt*astet*$bwe3&o6)'
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#CHANGE LATER TO USE .ENV

#print("HOST",os.getenv('ALLOWED_HOST'),"HOST TYPE",type(os.environ.get('ALLOWED_HOSTS')))

if os.environ.get('ALLOWED_HOSTS') is None:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")

if os.environ.get('CSFR_TRUSTED_ORIGINS') is None:
    CSFR_TRUSTED_ORGINS = []
else:
    CSFR_TRUSTED_ORGINS = os.environ.get('CSFR_TRUSTED_ORIGINS').split(" ")

    # Application definition
#print("ALLOWED_HOSTS",ALLOWED_HOSTS)
#print(os.environ.get('DB_USERNAME'))
#print(os.environ.get('DB_PASSWORD'))
#print(os.environ.get('DB_NAME'))
#print(os.environ.get('HOST'))
#print("PORT: ",os.environ.get('PORT'),"type: ",type(int(os.environ.get('PORT'))))

INSTALLED_APPS = [
    # our apps
    'Inventory.apps.InventoryConfig',
    'accounts.apps.AccountsConfig',
    'request.apps.RequestConfig',
    'register.apps.RegisterConfig',
    'crispy_forms',

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
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

 #CHANGE LATER TO USE .ENV VARIABLES
DATABASES = {
     'default': {
         'ENGINE': 'djongo',
         'NAME': 'hardDriveTrackerSystem',#os.environ.get('DB_NAME'),
         'CLIENT': {
             'username': os.environ.get('DB_USERNAME'), #os.environ.get('DB_USERNAME'),
             'password': os.environ.get('DB_PASSWORD'),#os.environ.get('DB_PASSWORD'),
             'host': 'db',#os.environ.get('HOST'), #os.environ.get('HOST'),
             'port': 27017#int(os.environ.get('PORT')),#int(os.environ.get('PORT')),
         }

     }
 }



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

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, '/').replace('\\','/'),
]


AUTH_USER_MODEL = 'accounts.User'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK="bootstrap4"

LOGIN_REDIRECT_URL="/login.html"
LOGOUT_REDIRECT_URL="/"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGGING = {
    'version': 1,
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './log.log',
            'formatter': 'simpleRe',
        },
    },
    'formatters': {
        'simpleRe': {
            'format': '{asctime} {message}',
            'style': '{',
        }
    }
}
