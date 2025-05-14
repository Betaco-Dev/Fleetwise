# Custom User Model
AUTH_USER_MODEL = 'Fleet_wise.User'  # Replace app_name with your app's name

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # Required for TokenAuthentication
    'drf_spectacular',  # Required for OpenAPI schema generation
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Token Authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Require authentication by default
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Fleet Management API',
    'DESCRIPTION': 'API documentation for the Fleet Management System.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # Exclude schema from direct serving
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'none',  # Collapse all sections by default
    },
}
