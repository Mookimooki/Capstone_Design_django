"""
Django settings for testRestApi project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wk@x73fg@&yz_2bq4(&culpl6m*ef0%o2l^znemn@cy3i(3*e3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','[::1]','13.125.229.163']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #user define
    'basicapi',         #user define
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware', #user define
]

MIDDLEWARE_CLASSES = (
    'phople.disable_CSRF.DisableCSRF',
)



ROOT_URLCONF = 'testRestApi.urls'

"""
#user define
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    )
}
"""

#upload media file ( photo )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
#user define
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',  #저장 할 파일 이름
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG', #레벨
            'propagate': True,
        },
    },
}
"""
#user define
"""
LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'myLog.log') 
LOGGING = { 
    'version': 1, 
    'disable_existing_loggers': False, 
    'formatters': { 
        'verbose': { 
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s", 
            'datefmt' : "%d/%b/%Y %H:%M:%S" 
        }, 
        'simple': { 
            'format': '%(levelname)s %(message)s' 
        }, 
    }, 
    'handlers': { 
        'file': { 
            'level': 'DEBUG', 
            'class': 'logging.handlers.RotatingFileHandler', 
            'filename': LOG_FILE, 
            'formatter': 'verbose', 
            'maxBytes':1024*1024*10, 
            'backupCount':5, 
        }, 
    }, 
    'loggers': { 
        'django': { 
            'handlers':['file'], 
            'propagate': True, 
            'level':'INFO', 
        }, 
        'django.request': { 
            'handlers':['file'], 
            'propagate': False, 
            'level':'INFO', 
        }, 
        'myAppName': { 
            'handlers': ['file'], 
            'level': 'DEBUG', 
        }, 
    } 
}
"""

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

WSGI_APPLICATION = 'testRestApi.wsgi.application'

""" This is default DB, but I changed it MongoDB.
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
   'default' : {
      'ENGINE' : 'djongo',
      'NAME' : 'django'
   }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'