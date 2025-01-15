from fastapi import APIRouter
from fastapi.responses import RedirectResponse



api_router = APIRouter()

@api_router.get("/")

async def read():
    return RedirectResponse('/docs')

#api_router.include_router(TokenRouter, prefix="/Token", tags=["Token"])
