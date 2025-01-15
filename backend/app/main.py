from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


from .api.v1.api import api_router as api_router_v1
from .core.config import settings as settings_value
from fastapi.responses import RedirectResponse




app = FastAPI(swagger_ui_parameters={"default_models_expand_depth": -1})

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings_value.project_display_name,
        version=settings_value.project_version,
        description=settings_value.project_description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if settings_value.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings_value.backend_cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)

# Redirect
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse('/docs')

# Router
app.include_router(api_router_v1, prefix=settings_value.api_str + "/v1")

