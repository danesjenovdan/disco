from .base import *

DEBUG = os.getenv("DJANGO_DEBUG", False)

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "changeme")

STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "static"))
STATIC_URL = os.getenv("DJANGO_STATIC_URL", "/static/")
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "/media/")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.getenv("DJANGO_DATABASE_HOST", "db"),
        "PORT": os.getenv("DJANGO_DATABASE_PORT", "5432"),
        "NAME": os.getenv("DJANGO_DATABASE_NAME", "wagtail"),
        "USER": os.getenv("DJANGO_DATABASE_USER", "wagtail"),
        "PASSWORD": os.getenv("DJANGO_DATABASE_PASSWORD", "changeme"),
    }
}

ALLOWED_HOSTS = ["localhost", "disco.lb.djnd.si", "disco.si"]
CSRF_TRUSTED_ORIGINS = ["https://disco.lb.djnd.si", "https://disco.si"]

# DJANGO STORAGE SETTINGS
if os.getenv("DJANGO_ENABLE_S3", False):
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = os.getenv("DJANGO_AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("DJANGO_AWS_SECRET_ACCESS_KEY", "")
    AWS_STORAGE_BUCKET_NAME = os.getenv("DJANGO_AWS_STORAGE_BUCKET_NAME", "djnd")
    AWS_DEFAULT_ACL = "public-read"  # if files are not public they won't show up for end users
    AWS_QUERYSTRING_AUTH = False  # query strings expire and don't play nice with the cache
    AWS_LOCATION = os.getenv("DJANGO_AWS_LOCATION", "disco")
    AWS_S3_REGION_NAME = os.getenv("DJANGO_AWS_REGION_NAME", "fr-par")
    AWS_S3_ENDPOINT_URL = os.getenv("DJANGO_AWS_S3_ENDPOINT_URL", "https://s3.fr-par.scw.cloud")
    AWS_S3_SIGNATURE_VERSION = os.getenv("DJANGO_AWS_S3_SIGNATURE_VERSION", "s3v4")
    AWS_S3_FILE_OVERWRITE = False  # don't overwrite files if uploaded with same file name

MAUTIC_URL = os.getenv('MAUTIC_URL', 'https://localhost/api/')
MAUTIC_USER = os.getenv('MAUTIC_USER', 'apiuser')
MAUTIC_PASS = os.getenv('MAUTIC_PASSWORD', 'apigeslo')

PODPRI_URL = os.getenv("PODPRI_URL", "https://localhost:8888/api/subscribe/")
SEGMENT_ID = os.getenv("SEGMENT_ID", 5)

REGISTRATION_SEGMENT = 30
REGISTERED_SEGMENT = 31
SCHOLARSHIP_SEGMENT = 32
PAID_SEGMENT = 33

try:
    from .local import *
except ImportError:
    pass
