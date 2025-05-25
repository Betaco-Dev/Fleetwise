AUTH_USER_MODEL = 'Fleetwise.User'  # Replace with your actual app name and model

RECAPTCHA_PUBLIC_KEY = "your-public-key" 
RECAPTCHA_PRIVATE_KEY = "your-private-key"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',  # Change this to match your MySQL database name
        'USER': 'your_mysql_user',  # Your MySQL username
        'PASSWORD': 'your_mysql_password',  # Your MySQL password
        'HOST': 'localhost',  # Change if using a remote MySQL server
        'PORT': '3306',  # MySQL default port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # Ensures strict MySQL behavior
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your actual SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'Fleetwise Security <your-email@example.com>'


INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'channels',
    'captcha',
]

ASGI_APPLICATION = 'Fleetwise.asgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Fleet Management API',
    'DESCRIPTION': 'API documentation for the Fleet Management System.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'none',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'security': {  # Security logs separate from debug logs
            'handlers': ['security_file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
