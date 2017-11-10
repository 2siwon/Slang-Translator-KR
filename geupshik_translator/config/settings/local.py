from .base import *

SECRET_KEY = config_secret_common['django']['secret_key']
DATABASES = config_secret_common['django']['databases']

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INSTALLED_APPS += [
    # 3rd-party
    'django_extensions',
    # Custom
    'translation',
    'text_to_speech',
]

