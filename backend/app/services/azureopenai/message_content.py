from typing import Optional

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate,image
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.output_parsers import PydanticOutputParser


from ..azureopenai.azure_openai_client import AzureOpenAIClient

#generate_message_content

class GenerateMessageServices:

    def __init__(self):
        self.azure_openai_client = AzureOpenAIClient()

    def generate_message_content(
        self,
        content: str,
        output_schema: BaseModel,
        system_message: str,
        image_url: Optional[str] = None,
    ) -> BaseModel:
        try:
            client:AzureChatOpenAI = self.azure_openai_client.azure_openai_client()

            # Use Langchain's PydanticOutputParser for schema
            parser = PydanticOutputParser(pydantic_object=output_schema)

            # Create prompt templates
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_message + "\n{format_instructions}",
                partial_variables={"format_instructions": parser.get_format_instructions()}
            )
            human_message_prompt = HumanMessagePromptTemplate.from_template(content)


            # Create the ChatPromptTemplate
            chat_prompt = ChatPromptTemplate.from_messages([
                system_message_prompt,
                human_message_prompt
            ])

            if image_url:
                chat_prompt.append(image(image_url))            

            # Generate the message content
            response = client.invoke(
                chat_prompt.format_prompt().to_messages()
            )

            # Parse the response
            parsed_response = parser.parse(response)

            return parsed_response

        except Exception as e:
            raise Exception(f"Error generating message content: {e}")
