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
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")


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
    'mptt',
    'simple_history',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'django_filters',
    'tinymce',
    'crispy_forms',
    'crispy_bootstrap5',

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
    # 'django.middleware.cache.UpdateCacheMiddleware',  # per-site CACHE
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',  # per-site CACHE
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
MPTT_ADMIN_LEVEL_INDENT = 20  # indent pixels per level globally

# DJANGO REST FRAMEWORK CONFIGURATIONS
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            save link image media preview codesample
            table code lists fullscreen  insertdatetime  nonbreaking
            directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking |
            ''',
    'menubar': False,
    'statusbar': False,
}

# Crispy bootstrap5 configurations
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# EMAIL CONFIGURATION
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')

# SEND LOG CONFIGURATION
ADMIN = [('ADMIN_NAME', 'ADMIN_EMAIL'), ]

# CACHE CONFIGURATIONS
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env.str('REDIS_LOCATION'),
    }
}
# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 120
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
