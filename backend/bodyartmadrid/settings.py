"""
Django settings for Body Art Madrid.

Configuracion de desarrollo con SQLite.
En produccion: cambiar SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, etc.
"""

from pathlib import Path
import os

# ============================================
# PATHS
# ============================================
# BASE_DIR = backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# PROJECT_DIR = raiz del repo (un nivel arriba de backend/)
PROJECT_DIR = BASE_DIR.parent


# ============================================
# SECURITY
# ============================================
# SECURITY WARNING: cambia esto en produccion!
SECRET_KEY = 'django-insecure-z8%$q76tvcjkjc83v5hp*dsklni$a2=@yv0)9p@$fh*8ase(&5'

# SECURITY WARNING: no uses DEBUG=True en produccion!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']


# ============================================
# APPS
# ============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # App principal del sitio
    'webapp',
]


# ============================================
# MIDDLEWARE
# ============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================
# URLS
# ============================================
ROOT_URLCONF = 'bodyartmadrid.urls'


# ============================================
# TEMPLATES
# ============================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================
# WSGI
# ============================================
WSGI_APPLICATION = 'bodyartmadrid.wsgi.application'


# ============================================
# DATABASE (SQLite para desarrollo)
# ============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================
# AUTH PASSWORD VALIDATORS
# ============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================
# INTERNACIONALIZACION
# ============================================
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True


# ============================================
# STATIC FILES (CSS, JS, imagenes del sitio)
# ============================================
# URL publica para archivos estaticos
STATIC_URL = '/static/'

# Directorios donde Django busca archivos estaticos adicionales (ademas de app/static/)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Carpeta donde collectstatic recopila todo para produccion
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ============================================
# MEDIA FILES (subidas del admin: galeria, etc.)
# ============================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ============================================
# DEFAULT PRIMARY KEY
# ============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
