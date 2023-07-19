from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-v*(q*imd0kln^!29=gx50#e^y)%4!fc_1!+u**0l_v76bzlh(&"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MAUTIC_URL = os.getenv('MAUTIC_URL', '')
MAUTIC_USER = os.getenv('MAUTIC_USER', '')
MAUTIC_PASS = os.getenv('MAUTIC_PASSWORD', '')

REGISTRATION_SEGMENT = 30
REGISTERED_SEGMENT = 31

PODPRI_URL = os.getenv("PODPRI_URL", "https://localhost:8888/api/subscribe/")
SEGMENT_ID = os.getenv("SEGMENT_ID", 5)

try:
    from .local import *
except ImportError:
    pass
