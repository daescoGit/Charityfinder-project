import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9&(1owf*mzwo5h1csq9p3-+z920ojprb*w(5=51rpjc!v%-fvu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# .env decoupled, default to prevent app breaking
GG_API_KEY = config('api_key', default='')
SENDINBLUE_KEY = config('sendinblue_key', default='')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # part of django-allauth config (signup)
    'django.contrib.sites',

    # 3rd-party apps
    'rest_framework',
    'rest_framework.authtoken',
    # pre-made django-rest-auth for login endpoint
    'rest_auth',
    # part of django-allauth config (signup, api)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    # RQ
    'django_rq',
    # mptt for comment hierarchy
    'mptt',

    # local
    'charityfinder_app',
    'login_app',
    'comment_app',
    'user_profile_app',
]

# Using a strong base permission and losing up on the individual views
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # for browsable API, client side log in, out
        'rest_framework.authentication.SessionAuthentication',
        # for passing auth credentials in http header
        'rest_framework.authentication.TokenAuthentication',
    ]
}

MIDDLEWARE = [
    'middleware.middleware.AntiSpamMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# docker run -p 6379:6379 redis
# python manage.py rqworker
RQ_QUEUES = {
   'default': {
      'HOST': 'localhost',
      'PORT': '6379',
      'DB': 0,
      'DEFAULT_TIMEOUT': 360,
   }
}

# Memcached with python-memcached binding
# default port 11211
# add locations to share cache over multiple servers
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

ROOT_URLCONF = 'charityfinder_project.urls'

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

WSGI_APPLICATION = 'charityfinder_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# uploaded images save/serve path
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# api-auth config
SITE_ID = 1
LOGIN_REDIRECT_URL = '/charityfinder/mypage'
ACCOUNT_LOGOUT_REDIRECT_URL = '/charityfinder'

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True ### <--- DON'T USE THIS - USE EMAIL_USE_TLS
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sender-email'
EMAIL_HOST_PASSWORD = SENDINBLUE_KEY
