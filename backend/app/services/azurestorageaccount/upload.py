import uuid
import os
from fastapi import UploadFile


from .azure_storage_client import AzureStorageAccountClient

class UploadService:
    def __init__(self):
        """
        Initialize an uploader for Azure Storage Account.

        This class handles the initialization of Azure Storage Account client and sets up 
        the container configuration for file uploads.

        Attributes:
            storage_client: A blob service client instance for Azure Storage operations.
            container_name: Name of the container in Azure Storage. Defaults to "uploads" if not specified in environment.
        """
        self.storage_client = AzureStorageAccountClient().get_blob_service_client()
        self.container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "uploads")  # Default container name

    async def upload_file(self, file: UploadFile):
        try:

            blob_name = f"{uuid.uuid4()}-{file.filename}"
            blob_client = self.storage_client.get_blob_client(container=self.container_name, blob=blob_name)
            await blob_client.upload_blob(file.file)
            return {"filename": blob_name, "url": blob_client.url}
        
        
        except Exception as e:
            raise Exception(f"Error uploading file to Azure Storage: {e}")