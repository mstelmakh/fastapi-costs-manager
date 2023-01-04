from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.settings import settings
from api.api import api_router

app = FastAPI(
    title=settings.title
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get('/')
def root():
    return {"message": "Hello"}
