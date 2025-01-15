from typing import  List, Union
from pydantic import AnyHttpUrl, EmailStr, BaseModel, field_validator
from pydantic_settings import BaseSettings

class Contact(BaseModel):
    name: str
    url: AnyHttpUrl
    email: EmailStr

class LicenseInfo(BaseModel):
    name: str
    url: AnyHttpUrl

class Settings(BaseSettings):
    api_str: str = "/api"
    server_name: str
    server_host: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    backend_cors_origins: List[AnyHttpUrl] = []

    @field_validator("backend_cors_origins")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    project_display_name: str
    project_description: str
    project_version: str
    terms_of_service: str
    contact: Contact
    license_info: LicenseInfo

settings = Settings(
    server_name="localhost",
    server_host="http://localhost:8000",
    backend_cors_origins=["http://localhost:8000"],
    project_display_name="FashionFusionAI",
    project_description="AI-powered fashion recommendation system",
    project_version="0.0.1",
    terms_of_service="http://example.com/terms",
    
    contact=Contact(
        name="serhanayberkkilic",
        url="https://github.com/serhanayberkkilic",
        email="serhanayberkkilic@gmail.com"
    ),
    
    license_info=LicenseInfo(
        name="MIT",
        url="https://opensource.org/licenses/MIT"
    )
)

