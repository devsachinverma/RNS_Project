import os
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
import boto3
from .encryption import generate_key, encrypt_file

class FileUploadView(View):
    def post(self, request):
        uploaded_file = request.FILES['file']
        temp_file_path = default_storage.save(uploaded_file.name, uploaded_file)
        
        # Generate an encryption key and encrypt the file
        key = generate_key()
        encrypt_file(temp_file_path, key)
        
        # Upload the encrypted file to S3
        s3_client = boto3.client('s3', 
                                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                  region_name=settings.AWS_S3_REGION_NAME)
        
        with open(temp_file_path, 'rb') as file:
            s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, uploaded_file.name)
        
        # Clean up the local file
        os.remove(temp_file_path)

        return JsonResponse({'message': 'File uploaded and encrypted successfully!', 'key': key.decode()})
