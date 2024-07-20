"""
Django settings for django_crud_api project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jw!vs1@gw*a3v9xo7cwnz#d573==em%rwxc$8w$4#d@yb(nh(='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'coreapi',
    'tasks',
    'authentication',
    'OpenWeather',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    #'BackDjango.debug_middleware.DebugMiddleware',  # Añadir aquí
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authentication.middleware.AutoLogoutMiddleware',
]

ROOT_URLCONF = 'django_crud_api.urls'

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

WSGI_APPLICATION = 'django_crud_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_ingresos',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_CREDENTIALS = True  # Permitir el envío de cookies y encabezados de autenticación
CORS_ALLOWED_ORIGINS = [ "http://localhost:3000",]

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Agrega esta línea
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# JWT settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
}

# Seguridad de cookies
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False # SESSION_COOKIE_SECURE y CSRF_COOKIE_SECURE: Deben estar en True para garantizar que las cookies solo se envíen a través de HTTPS.
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_HTTPONLY = False # SESSION_COOKIE_HTTPONLY y CSRF_COOKIE_HTTPONLY: Configurados en True para que las cookies no sean accesibles a través de JavaScript, lo que ayuda a prevenir ataques XSS.
SESSION_COOKIE_SAMESITE = 'Lax'  
CSRF_COOKIE_SAMESITE = 'Lax' # SESSION_COOKIE_SAMESITE y CSRF_COOKIE_SAMESITE: Configurados en 'Lax' o 'Strict' para mitigar ataques CSRF. 'Lax' suele ser una buena opción por usabilidad y seguridad.


# Importar default_headers correctamente
from corsheaders.defaults import default_headers
# Opcionalmente, permitir todas las cabeceras de CORS
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
    # Otros encabezados necesarios
]

# Configuración CSRF
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']  # URL de tu frontend

# Seguridad de la aplicación
SECURE_BROWSER_XSS_FILTER = True # Activa el filtro XSS del navegador.
SECURE_CONTENT_TYPE_NOSNIFF = True # Previene ataques de tipo MIME.
X_FRAME_OPTIONS = 'DENY' # Configurado en 'DENY' para evitar que tu sitio sea incluido en un iframe, previniendo ataques de clickjacking

# Seguridad para HTTPS
SECURE_SSL_REDIRECT = not DEBUG #Redirige todo el tráfico HTTP a HTTPS. Solo debería estar activo en producción (not DEBUG)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configuración de la sesión
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db' # Utiliza una base de datos en caché para las sesiones, lo que puede mejorar el rendimiento.
SESSION_COOKIE_AGE = 1800  # 30 minutes
SESSION_SAVE_EVERY_REQUEST = True # Guarda la sesión en cada solicitud.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # Expira la sesión cuando se cierra el navegador.