
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True  # Set to False for production

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")


SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_COOKIE_NAME = "auth0_simple_django_session"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"] # , "yourdomain.com"]  # Add your domain for production


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "auth0_auth"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "auth0_integration.urls"


AUTHLIB_OAUTH_CLIENTS = {
    "auth0": {
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
        "client_secret": os.getenv("AUTH0_CLIENT_SECRET"),
        "api_base_url": os.getenv("AUTH0_BASE_URL"),
        "access_token_url": os.getenv("AUTH0_BASE_URL") + "/oauth/token",
        "authorize_url": os.getenv("AUTH0_BASE_URL") + "/authorize",
        #"userinfo_url": os.getenv("AUTH0_BASE_URL") + "/userinfo",
        "redirect_uri": "http://localhost:8863/callback",  # Change the port as needed
        "jwks_uri": os.getenv("AUTH0_BASE_URL") + "/.well-known/jwks.json",
        "client_kwargs": {
            "scope": "openid profile email",
        },
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "auth0_integration.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
