from fastapi import APIRouter
from fastapi.responses import RedirectResponse

###### For Create Models ######
from App.Database import Models
###### For Create Models ######

from App.Api.V1.Endpoints.Token.Token import Router as TokenRouter


from App.Api.V1.Endpoints.Organization.Organization import Router as OrganizationRouter
from App.Api.V1.Endpoints.Organization.Default import Router as OrganizationDefaultRouter



api_router = APIRouter()

@api_router.get("/")

async def read():
    return RedirectResponse('/docs')

api_router.include_router(TokenRouter, prefix="/Token", tags=["Token"])

api_router.include_router(OrganizationRouter, prefix="/Organization", tags=["Organization"])

