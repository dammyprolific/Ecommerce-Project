from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers
import dj_database_url
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-dev-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'



ALLOWED_HOSTS = ["shopwithdammy.onrender.com", "localhost", "127.0.0.1"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Local apps
    'coreUsers',
    'Shopping_App',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Ecommerce.wsgi.application'


if os.getenv("RENDER") == "True":  # Add this in your Render environment
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=False  # Disable SSL for local PostgreSQL
        )
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'coreUsers.CustomUsers'

BASE_URL = "http://127.0.0.1:8000"

BASE_URL = "http://localhost:5173"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://shop-c9zj.onrender.com"
]

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'authorization',
# ]
CORS_ALLOW_ALL_ORIGINS = True 

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
}

# FLUTTERWAVE_PUBLIC_KEY = os.environ.get("FLUTTERWAVE_PUBLIC_KEY", "FLWPUBK_TEST-373a09fd7168ed31f75f6812aedde1c3-X")
# Add your actual secret key here. Replace the value with your real Flutterwave secret key.
FLUTTERWAVE_SECRET_KEY = os.environ.get('FLUTTERWAVE_SECRET_KEY', 'FLWSECK_TEST-5178b0f76422f10d30d9457cb284a344-X')
# ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', 'FLWSECK_TESTcbc308ee7dae')

PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID", "ARWe8mgWX6U5lYZOA2_eCEdCqn626MAykueQ0Chug-VqNDgJiIMlS5QrBRvr_Hh1R9KDlHpAeU0d3aC0")
PAYPAL_SECRET_KEY = os.environ.get("PAYPAL_SECRET_KEY", "EBrLuxHP_VZUz7tMGKtDDprzV1yps3wIHXQzXwS_PAaOr77_CYFxZWv50fmmbnpWFaKdDnEBcX3WOWY5")
PAYPAL_MODE = 'live'

REACT_BASE_URL = os.getenv("REACT_BASE_URL" ,"http://localhost:5173")


