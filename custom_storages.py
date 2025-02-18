from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'  # Specify the directory for static files
    file_overwrite = False  # To prevent overwriting files

class MediaStorage(S3Boto3Storage):
    location = 'media'  # Specify the directory for media files
    file_overwrite = False  # To prevent overwriting files