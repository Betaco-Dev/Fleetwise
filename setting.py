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
}
