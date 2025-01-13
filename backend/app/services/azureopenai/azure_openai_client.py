import os

from langchain_openai import AzureChatOpenAI

class AzureOpenAIClient:

    def __init__(self):
        try:
            self.azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
            self.azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            self.azure_openai_model = os.getenv("AZURE_OPENAI_MODEL")
            self.azure_openai_model_upper = os.getenv("AZURE_OPENAI_MODEL_UPPER")
            self.azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")

        except Exception as e:
            raise Exception(f"Error getting environment variables: {e}")

    def azure_openai_client(self) -> AzureChatOpenAI:
        try:
            client = AzureChatOpenAI(
                api_key=self.azure_openai_api_key,
                azure_endpoint=self.azure_openai_endpoint,
                api_version=self.azure_openai_api_version,
                deployment_name=self.azure_openai_model,  # Specify the deployment name
                response_format={"type": "json_object"}
            )
            
            return client
        except Exception as e:
            raise Exception(f"Error creating Azure OpenAI client: {e}")