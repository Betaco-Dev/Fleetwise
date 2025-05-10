# settings.py
AUTH_USER_MODEL = 
  'models.User'


INSTALLED_APPS = [
  ... 
  'rest_framework',
]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
  'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
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
}
