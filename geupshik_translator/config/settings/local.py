from .base import *

SECRET_KEY = config_secret_common['django']['secret_key']
DATABASES = config_secret_common['django']['databases']

INSTALLED_APPS += [
    # 3rd-party
    'django_extensions',
    # Custom
    'translation',
]
