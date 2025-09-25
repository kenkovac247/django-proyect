import os
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get('AWS_BUCKET_MEDIA', 'tu-proyecto-media')
    location = 'media'
    file_overwrite = False
    
    def __init__(self, *args, **kwargs):
        kwargs['bucket_name'] = self.bucket_name
        super().__init__(*args, **kwargs)