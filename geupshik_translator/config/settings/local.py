from .base import *

SECRET_KEY = config_secret_common['django']['secret_key']
DATABASES = config_secret_common['django']['databases']

INSTALLED_APPS += [
    # 3rd-party
    'django_extensions',
    'rest_framework',
    # Custom
    'translations',
]

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     )
# }