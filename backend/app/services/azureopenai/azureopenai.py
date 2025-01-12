import os
import json

from openai import AzureOpenAI

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


from pydantic import BaseModel
import mimetypes

from backend.app.schemas.services.azureopenai.output import CompletionResponse



class AzureOpenAIClass:


    def __init__(self):
        try:
            
            self.AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
            self.AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
            self.AZURE_OPENAI_MODEL = os.getenv("Azure_OPENAI_MODEL")
            self.AZURE_OPENAI_MODEL_UPPER = os.getenv("Azure_OPENAI_MODEL_UPPER")
            self.Azure_OPENAI_API_VERSION = os.getenv("Azure_OPENAI_API_VERSION")
        
        except Exception as error:
            raise Exception(f"Failed to load environment variables: {str(error)}")

    def azure_openai_client(self) -> AzureOpenAI:
            
            try:
                
                client = AzureOpenAI(
                                    api_key = self.AZURE_OPENAI_API_KEY,
                                    azure_endpoint = self.AZURE_OPENAI_ENDPOINT,
                                    api_version = self.Azure_OPENAI_API_VERSION
                                    ) 
                
                return client
            
            except Exception as error:
                
                raise Exception(f"Failed to create Azure OpenAI client: {str(error)}")

    def generate_message_content(self,
                                 content:str,
                                 output_schema:BaseModel,
                                 system_message:str,
                                 image_url:str=None,
                                 temperature:float=0.0,
                                 max_tokens:int=1000,
                                 top_p:float=1.0,
                                 ) -> CompletionResponse: 
        
        try:
            
            client = self.azure_openai_client()

            # Set up a parser + inject instructions into the prompt template.
            parser = PydanticOutputParser(pydantic_object=output_schema)
    
            prompt = PromptTemplate(
                template="{format_instructions}",
                partial_variables={"format_instructions": parser.get_format_instructions()},
            )

            # Format the prompt
            formatted_prompt = prompt.format()


            # Create a list of messages to send to the model
            messages = [
                {
                    "role": "system", 
                    "content": (
                        "systemMessage:"f"{system_message}"
                        "schemas:"f"{formatted_prompt}"
                    )
                }
            ]


            # Add the OCR CV result to the messages
            messages.append({"role": "user", "content": content})

            # Add the image URL to the messages

            if image_url:
                mime_type, _ = mimetypes.guess_type(ImageUrl)

                if mime_type and mime_type.startswith('image'):
                        # Resim URL'si ise
                        messages.append({
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": ImageUrl
                                    }
                                }
                            ]
                        })



            # Send the messages to the model
            response =client.chat.completions.create(
                model=self.AZURE_OPENAI_MODEL,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                response_format={"type": "json_object"}
            ) 


            # Return the content as a JSON object
            return response

        
        
        except Exception as error:
            
            raise Exception(f"Failed to create  document from text: {str(error)}")
