import os
from ..azurestorageaccount.azure_storage_client import AzureStorageAccountClient

class DeleteService:


    def __init__(self):
        """
        Initializes an Azure Storage Account Delete Service.

        This constructor sets up the necessary Azure Storage client and container configuration
        for blob deletion operations.

        Attributes:
            storage_client: Azure Blob Service client instance for storage operations
            container_name: Name of the Azure Storage container (defaults to "uploads")

        Raises:
            Exception: If initialization of Azure Storage Account client fails
        """
        try:
            self.storage_client = AzureStorageAccountClient().get_blob_service_client()
            self.container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "uploads")  # Default container name
        except Exception as e:
            raise Exception(f"Error initializing Azure Storage Account client: {e}")

    async def delete_file(self, filename: str):
        try:
            blob_client = self.storage_client.get_blob_client(container=self.container_name, blob=filename)
            await blob_client.delete_blob()
            return {"status": "success", "message": f"File '{filename}' deleted successfully."}
        except Exception as e:
            raise Exception(f"Error deleting file from Azure Storage: {e}")