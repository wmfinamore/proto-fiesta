import os
from pathlib import Path
from environs import Env
from decouple import config

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env("DJANGO_SECRET_KEY")
SECRET_KEY = env("DJANGO_SECRET_KEY", config("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DJANGO_DEBUG", default=False)
DEBUG = True

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", config("DJANGO_ALLOWED_HOSTS")).split(" ")

# Application definition

INSTALLED_APPS = [
    # custom site admin
    'config.apps.ProtoAdminConfig',

    # django native apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # será necessário realizar um novo build da imagem (--build)
    'cpf_field',
    'cnpj_field',

    # 3thd
    'debug_toolbar',
    'bootstrapform',
    'mptt',
    'simple_history',
    'rest_framework',
    'drf_yasg',
    'django_filters',

    # local apps
    'accounts',
    'apps.core',
    'apps.cargos',
    'apps.orgaos',
    'apps.assuntos',
    'apps.processos',
    'apps.tramitacoes',
    'apps.api',
    'apps.interessados',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME", config('DBL_NAME')),
        'USER': env("DB_USER", config('DBL_USER')),
        'PASSWORD': env("DB_PASSWORD", config('DBL_PASSWORD')),
        'HOST': env("DB_HOST", config('DBL_HOST')),
        'PORT': env("DB_PORT", config('DBL_PORT'))
    },
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

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA FILES
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DEBUG TOOLBAR CONFIGURATION
INTERNAL_IPS = [
    '127.0.0.1',
]

# CONFIGURATION TO USE CUSTOMER MODEL
AUTH_USER_MODEL = 'accounts.CustomUser'

# LOGIN/LOGOUT CONFIGURATION
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# MPTT CONFIGURATIONS
MPTT_ADMIN_LEVEL_INDENT = 20 # indent pixels per level globally

# DJANGO REST FRAMEWORK CONFIGURATIONS
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
