# Django settings for jidox project.

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-suf^3!11jptsia##mi_!vw$p8z&o^$=)(%c7ua%##m$n0tmqa^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
 #   "django_extensions",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    'crispy_bootstrap5',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]
LOCAL_APPS = [
    "users.apps.UsersConfig",
    "apps.apps.AppsConfig",
    "custom.apps.CustomConfig",
    "components.apps.ComponentsConfig",
    "layouts.apps.LayoutsConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Add the required authentication backends for django-allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Add AccountMiddleware for django-allauth
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # Add this line for AccountMiddleware
]

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"

ROOT_URLCONF = "jidox.urls"

import os

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "jidox.wsgi.application"


# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'mssql', # Installed MSSQL Engine
        'NAME': 'db.mssql-jidox1', # MSSQL Database Name
        'USER': '',  # Windows authentication leaves this blank
        'PASSWORD': '',  # Windows authentication leaves this blank
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Ensure this matches your installed driver
            'trusted_connection': 'yes',  # Enables Windows Authentication
        },
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user model
AUTH_USER_MODEL = "users.User"


# django-allauth settings
ACCOUNT_ALLOW_REGISTRATION = True
#ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_LOGIN_METHODS = {'username', 'email'}

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"

SITE_ID = 1

# Social account provider settings (if you plan to use social login)
SOCIALACCOUNT_PROVIDERS = {}

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
