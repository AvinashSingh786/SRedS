"""
Django settings for W3RS project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# @TODO NB! PLEASE CHANGE THIS KEY IF YOU PLAN TO USE IN PRODUCTION
SECRET_KEY = '==snqksaq+(sfvr2^hg90-7&&^pfxut(&r*o#)fpzm83a)famu'

# @TODO SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# @TODO CHANGE TO ONLY ALLOW PRODUCTION SERVER DOMAINS and IPs
ALLOWED_HOSTS = ['*']

# Application definition
PROJECT_NAME = 'SecureRS'

COMPANY_NAME = 'Avinash Singh'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'otp_yubikey',
    'sslserver',
    'pde',
    'rest_framework',
    'rest_framework_api_key',
    # "djangosecure",
    'session_security',
    'encrypted_files'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    # "djangosecure.middleware.SecurityMiddleware",
    'session_security.middleware.SessionSecurityMiddleware',
]

 

ROOT_URLCONF = 'SecureRS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.meta',

            ],
        },
    },
]

FILE_UPLOAD_HANDLERS = [
    "handler.uploadhandler.HashFileUploadHandler",
    "encrypted_files.uploadhandler.EncryptedFileUploadHandler",
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]

WSGI_APPLICATION = 'SecureRS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# Add your own database config for MYSQL, consult link above

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # 'static'
]

LOGIN_URL = 'two_factor:login'

# this one is optional
LOGIN_REDIRECT_URL = 'two_factor:profile'
LOGOUT_REDIRECT_URL = '/'

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True


DEFAULT_FILE_STORAGE = "randomfilestorage.storage.RandomFileSystemStorage"
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SITE_URL = "https://localhost:8000/"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework_api_key.permissions.HasAPIKey',
    )
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # @TODO Remove to use SMTP
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''  # @TODO change details
EMAIL_HOST_PASSWORD = ''  # @TODO change details

DEFF_SALT = "Aasd^*&$E%%#FVTB"  # @TODO change details
DEFF_PASSWORD = "SeC#RS_D3m0"  # @TODO change details
DEFF_FETCH_URL_NAME = "" 
CRYPTOGRAPHY_SALT = "RS_D3m0"
AES_KEY = b"ecnxgffjomxmqrtlyzrskiudiivztxyk"

SUSPICIOUS = 10  # This goes in hand with the rank parameter in the PDE
MALICIOUS = 18    # This goes in hand with the rank parameter in the PDE

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SECURITY_WARN_AFTER = 350
SESSION_SECURITY_EXPIRE_AFTER = 50000

