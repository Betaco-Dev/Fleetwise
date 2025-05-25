AUTH_USER_MODEL = 'Fleetwise.User'  # Replace with your actual app name and model

RECAPTCHA_PUBLIC_KEY = "your-public-key"
RECAPTCHA_PRIVATE_KEY = "your-private-key"


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
