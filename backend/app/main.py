from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


from app.api.v1.api import api_router as api_router_v1
from app.core.config import settings as settings_value




app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})





def CustomOpenapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings_value.project_name,
        version=settings_value.project_version,
        description=settings_value.project_description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = CustomOpenapi

if settings_value.backendCorsOrigins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings_value.backendCorsOrigins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


from starlette.requests import Request
from starlette.responses import Response
from fastapi.responses import RedirectResponse
from fastapi_pagination import add_pagination

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)



#################Redirect#################
@app.get("/")

async def read():
    return RedirectResponse('/docs')

############Router#################
app.include_router(api_router_v1, prefix=settings_value.api_str+"/v1")

add_pagination(app)