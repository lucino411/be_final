from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import environ
import dj_database_url # type: ignore
import sys


BASE_DIR = Path(__file__).resolve().parent.parent
# print(f"BASE_DIR: {BASE_DIR}")

# Initialize environ
# env = environ.Env(
#     # Set casting, default value
#     DEBUG=(bool, False)
# )

# Take environment variables from .env file
# Read the .env file
# environ.Env.read_env()
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Debug print statements to check if environment variables are loaded
# print("DB_ENGINE:", env('DB_ENGINE'))
# print("DB_NAME:", env('DB_NAME'))
# print("DB_USER:", env('DB_USER'))
# print("DB_PASSWORD:", env('DB_PASSWORD'))
# print("DB_HOST:", env('DB_HOST'))
# print("DB_PORT:", env('DB_PORT'))


SECRET_KEY = 'django-insecure-&e1g(n7j@yxzln$v1er7y(s02!j44x%mx7tl#i%&q43n$l_)r*'
# SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())
DEBUG=True
# DEBUG = env.bool('DEBUG', False)
# ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['161.35.52.52', '134.209.212.151', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['134.209.212.151', 'becrm.site', 'www.becrm.site', 'localhost', '127.0.0.1']

# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administration.userprofile',
    'administration.core',
    'administration.organization',
    'configuration.country',
    'configuration.product',
    'configuration.currency',
    'operation.dashboard',
    'operation.lead',
    'operation.deal',
    'operation.contact',
    'operation.client',
    'operation.company',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'administration.organization.context_processors.organization_details',
                'operation.lead.context_processors.lead_statistics',
                'operation.lead.context_processors.lead_task_statistics',
                'operation.deal.context_processors.deal_statistics',
                'operation.deal.context_processors.deal_task_statistics',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',       
#     }
# }

#database droplet root
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',     
#     }
# }

#database droplet blasil
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'be_final_bd',
        'USER': 'blasil',
        'PASSWORD': 'America123',
        'HOST': 'localhost',
        'PORT': '',     
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DB_ENGINE', default='django.db.backends.postgresql_psycopg2'),
#         'NAME': os.environ.get('DB_NAME', default=''),
#         'USER': os.environ.get('DB_USER', default=''),
#         'PASSWORD': os.environ.get('DB_PASSWORD', default=''),
#         'HOST': os.environ.get('DB_HOST', default=''),
#         'PORT': os.environ.get('DB_PORT', default=''),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql_psycopg2'),
#         'NAME': env('DB_NAME', default='defaultdb'),
#         'USER': env('DB_USER', default='doadmin'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST', default='db-postgresql-nyc3-12415-be-final-do-user-16579933-0.c.db.ondigitalocean.com'),
#         'PORT': env('DB_PORT', default='25060'),
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }

# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
# }

# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }



# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# if DEVELOPMENT_MODE is True:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }

# print("DB_NAME:", os.environ.get('DB_NAME'))


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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio para collectstatic en producción

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / Path('media')
LOGOUT_REDIRECT_URL = '/'

# if not DEBUG:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_HSTS_SECONDS = 31536000  # 1 year
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     X_FRAME_OPTIONS = "DENY"