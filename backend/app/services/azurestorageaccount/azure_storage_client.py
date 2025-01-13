import os
from azure.storage.blob import BlobServiceClient

class AzureStorageAccountClient:


    def __init__(self):
        try:
            connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
            if not connection_string:
                raise ValueError("Azure Storage Connection String environment variable is not set.")
            self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        except Exception as e:
            raise Exception(f"Error connecting to Azure Storage Account: {e}")

    def get_blob_service_client(self):
        try:
            return self.blob_service_client
        except Exception as e:
            raise Exception(f"Error getting blob service client: {e}")