from .base import *


SECRET_KEY = config_secret_common['django']['secret_key']
DATABASES = config_secret_common['django']['databases']

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
