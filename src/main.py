"""Entry point."""
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware

from src.configs.server_config import get_config
from src.init import shutdown_handler, startup_handler
from src.routers import common
from src.routers.v1 import cars as cars_v1
from src.routers.v2 import cars as cars_v2


config = get_config()

app = FastAPI(
    title=config.service,
    version=config.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_middleware(
    PrometheusMiddleware,
    app_name=config.service,
    prefix='http',
    buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 10.0, 30.0, 60.0, 180.0, 300.0]
)

app.add_event_handler('startup', startup_handler(app))
app.add_event_handler('shutdown', shutdown_handler(app))

app.include_router(common.router, tags=['Service status'])

v1 = APIRouter(tags=['Cars'], prefix='/v1')
v1.include_router(cars_v1.router)
app.include_router(v1)

v2 = APIRouter(tags=['Cars'], prefix='/v2')
v2.include_router(cars_v2.router)
app.include_router(v2)
