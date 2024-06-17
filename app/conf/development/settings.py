import os 
import warnings
from os.path import dirname, abspath, join

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv



load_dotenv()

warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))
CONTENT_DIR = join(BASE_DIR, 'content')

SECRET_KEY = 'NhfTvayqggTBPswCXXhWaN69HuglgZIkM'

DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Vendor apps
    'bootstrap4',

    # Application apps
    'main',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(CONTENT_DIR, 'templates'),
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

WSGI_APPLICATION = 'app.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "rpa.roober@gmail.com"
EMAIL_HOST_PASSWORD = "fcgo nvuw zldu lbbf"
DEFAULT_FROM_EMAIL = 'Ativação de conta <rpa.roober@gmail.com>'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', 'your_db_name'),
        'USER': os.getenv('DATABASE_USER', 'your_db_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '3306'),
    }
}

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

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
LANGUAGE_CODE = 'pt-br'
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('pt-br', _('Portuguese (Brazil)')),
]

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    join(CONTENT_DIR, 'locale')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH_USER_MODEL='email'